from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QSizePolicy

from config import WINDOW, RESET, SAFETY_LIMIT, CARD_MIN, CARD_MAX
from display import Display_Window
from player import Player
from custom_widgets import *

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Twilight Imperium Scoreboard"
        self.players = []
        self.players_set = False
        self.display = Display_Window(self)
        self.current_turn = 1
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(
            WINDOW["XPOS"],
            WINDOW["YPOS"],
            WINDOW["WIDTH"],
            WINDOW["HEIGHT"]
        )
        self.setStyleSheet("background-color:lightgray")
        self.add_menu()
        self.refresh_widgets()

    def add_player(self):
        index = len(self.players)
        player_num = index + 1
        self.players.append(Player(player_num))
        self.players[index].widget = Player_Widget(
            self.players[index],
            self.display
        )
        self.refresh_widgets()

    def refresh_widgets(self):
        if self.players:
            self.central_widget.setParent(None)
        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout()
        if self.players:
            for player in self.players:
                player.widget = Player_Widget(player, self.display)
                self.central_layout.addWidget(player.widget)
        if not self.players_set:
            self.add_player_button = Button("Add Player", self.add_player)
            self.add_player_button.setSizePolicy(
                QSizePolicy.Preferred, QSizePolicy.Expanding
            )
            self.central_layout.addWidget(self.add_player_button)
        else:
            self.current_turn = 0
            vbox = QVBoxLayout()
            next_turn = Button("Next", self.next_turn)
            next_turn.setSizePolicy(
                QSizePolicy.Preferred, QSizePolicy.Expanding
            )
            vbox.addWidget(next_turn)
            last_turn = Button("Last", self.last_turn)
            last_turn.setSizePolicy(
                QSizePolicy.Preferred, QSizePolicy.Expanding
            )
            vbox.addWidget(last_turn)
            reset = Button("Reset", self.reset)
            reset.setSizePolicy(
                QSizePolicy.Preferred, QSizePolicy.Expanding
            )
            vbox.addWidget(reset)
            self.central_layout.addLayout(vbox)
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

    def next_turn(self):
        self.turn_finder_loop(1)

    def last_turn(self):
        self.turn_finder_loop(-1)

    def turn_finder_loop(self, modifier):
        x = True
        turn_counter = 0
        while(x):
            turn_counter += 1
            if turn_counter >= SAFETY_LIMIT:
                self.soft_reset()
                self.display.update()
                break
            x = self.change_turn(modifier)

    def change_turn(self, modifier):
        for player in self.players:
            if player.is_turn:
                player.is_turn = False
        self.current_turn += modifier
        current_player = self.find_current_turn()
        if current_player:
            self.display.update()
            return False
        else:
            return True

    def find_current_turn(self):
        if self.current_turn < CARD_MIN:
            self.current_turn = CARD_MAX
        if self.current_turn > CARD_MAX:
            self.current_turn = CARD_MIN
        player_with_card = 0
        for player in self.players:
            if self.current_turn == player.strat_card:
                if not player.passed:
                    player.is_turn = True
                    player_with_card = player.num
        return player_with_card

    def soft_reset(self):
        for player in self.players:
            player.is_turn = False
            player.card_used = False

    def reset(self):
        self.soft_reset()
        for player in self.players:
            player.strat_card = 0
            player.passed = False
        self.display.update()
        self.refresh_widgets()

    def add_menu(self):
        menu = self.menuBar()

        file_menu = menu.addMenu('File')
        exit_option = Action(
            name='Exit',
            window=self,
            shortcut='Ctrl+Q',
            tip='Exit Program',
            func=self.close
        )
        file_menu.addAction(exit_option)

        display_menu = menu.addMenu('Display')
        display_option = Action(
            name='Open Scoreboard Display',
            window=self,
            shortcut='Ctrl+D',
            tip='Open Display in new window',
            func=self.open_display
        )
        display_menu.addAction(display_option)

        remove_option = Action(
            name='Remove "Add Player" Button',
            window=self,
            shortcut='Ctrl+R',
            tip='Remove "Add Player" button from interface',
            func=self.remove_button
        )
        display_menu.addAction(remove_option)

    def open_display(self):
        self.display.show()

    def remove_button(self):
        self.players_set = True
        self.refresh_widgets()

    def close(self):
        super().close()

    def get_players(self):
        return self.players
