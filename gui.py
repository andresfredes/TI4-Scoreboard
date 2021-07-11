from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QSizePolicy

from config import WINDOW
from display import Display_Window
from player import Player
from custom_widgets import *

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Twilight Imperium Scoreboard"
        self.players = []
        self.display = Display_Window()
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
        self.add_player_button = Button("Add Player", self.add_player)
        self.add_player_button.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding
        )
        self.central_layout.addWidget(self.add_player_button)
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

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
        add_option = Action(
            name='Open Scoreboard Display',
            window=self,
            shortcut='Ctrl+D',
            tip='Open Display in new window',
            func=self.open_display
        )
        display_menu.addAction(add_option)

    def open_display(self):
        self.display.show()

    def close(self):
        super().close()
