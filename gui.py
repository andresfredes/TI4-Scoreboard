from PyQt5.QtWidgets import (QMainWindow, QAction, QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QSizePolicy, QComboBox)

from config import *
from display import Display_Window

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Twilight Imperium Scoreboard"
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self.xpos = WINDOW_XPOS
        self.ypos = WINDOW_YPOS
        self.players = []
        self.display = Display_Window()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.xpos, self.ypos, self.width, self.height)
        self.add_menu()
        self.refresh_widgets()

    def add_player(self):
        index = len(self.players)
        player_num = index + 1
        self.players.append(Player(player_num))
        self.players[index].widget = Player_Widget(self.players[index])
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
        self.add_player_button = QPushButton(self)
        self.add_player_button.setText("Add Player")
        self.add_player_button.clicked.connect(self.add_player)
        self.add_player_button.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding
        )
        self.central_layout.addWidget(self.add_player_button)
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

    def add_menu(self):
        menu = self.menuBar()

        file_menu = menu.addMenu('File')
        exit_option = QAction('Exit', self)
        exit_option.setShortcut('Ctrl+Q')
        exit_option.setStatusTip('Exit Program')
        exit_option.triggered.connect(self.close)
        file_menu.addAction(exit_option)

        display_menu = menu.addMenu('Display')
        add_option = QAction('Open Scoreboard Display', self)
        add_option.setShortcut('Ctrl+D')
        add_option.setStatusTip('Open Display in new window')
        add_option.triggered.connect(self.open_display)
        display_menu.addAction(add_option)

    def open_display(self):
        self.display.show()

    def close(self):
        super().close()

class Player(object):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.name = ""
        self.faction = None
        self.colour = None
        self.score = 0
        self.strat_card = 0
        self.passed = False
        self.card_used = False

class Player_Widget(QWidget):
    def __init__(self, player, display):
        super().__init__()
        self.player = player
        self.display = display
        self.init_UI()
        self.load_player_data()

    def init_UI(self):
        vbox = QVBoxLayout()
        player_label = QLabel()
        player_label.setText("Player " + str(self.player.num))
        vbox.addWidget(player_label)

        hbox1 = QHBoxLayout()
        self.player_name = QLineEdit()
        hbox1.addWidget(self.player_name)
        set_button = QPushButton()
        set_button.setText("Set Name")
        set_button.clicked.connect(self.set_name)
        hbox1.addWidget(set_button)
        vbox.addLayout(hbox1)

        self.faction = QComboBox()
        self.faction.addItems(FACTIONS)
        self.faction.activated.connect(self.set_faction)
        vbox.addWidget(self.faction)

        self.colour = QComboBox()
        self.colour.addItems(COLOURS.keys())
        self.faction.activated.connect(self.set_colour)
        vbox.addWidget(self.colour)

        self.strat_card = QComboBox()
        self.strat_card.addItems(STRAT_CARDS.values())
        self.strat_card.activated.connect(self.set_strat_card)
        vbox.addWidget(self.strat_card)

        hbox2 = QHBoxLayout()
        self.used_button = QPushButton()
        self.used_button.setText("Card active")
        self.used_button.clicked.connect(self.used_card_toggle)
        hbox2.addWidget(self.used_button)
        self.passed_button = QPushButton()
        self.passed_button.setText("Player active")
        self.passed_button.clicked.connect(self.passed_toggle)
        hbox2.addWidget(self.passed_button)
        vbox.addLayout(hbox2)

        hbox3 = QHBoxLayout()
        minus_button = QPushButton()
        minus_button.setText("-")
        minus_button.clicked.connect(self.score_minus)
        hbox3.addWidget(self.minus_button)
        self.score = QLabel()
        self.score.setText(str(self.player.score))
        plus_button = QPushButton()
        plus_button.setText("+")
        plus_button.clicked.connect(self.score_plus)
        hbox3.addWidget(self.plus_button)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)

    def update_display(func):
        def inner(self):
            func()
            self.display.update(self.player)
        return inner

    @update_display
    def set_name(self):
        self.player.name = self.player_name.text()

    @update_display
    def set_faction(self):
        self.player.faction = self.faction.currentText()

    @update_display
    def set_colour(self):
        self.player.colour = self.colour.currentText()

    @update_display
    def set_strat_card(self):
        self.player.strat_card = self.strat_card.currentText()

    @update_display
    def used_card_toggle(self):
        if self.player.card_used:
            self.used_button.setText("Card active")
            self.player.card_used = False
        else:
            self.used_button.setText("Card used")
            self.player.card_used = True

    @update_display
    def passed_toggle(self):
        if self.player.passed:
            self.passed_button.setText("Player active")
            self.player.passed = False
        else:
            self.passed_button.setText("Player passed")
            self.player.passed = True

    def update_score(func):
        def inner(self):
            func()
            self.score.setText(str(self.player.score))
        return inner

    @update_display
    @update_score
    def score_minus(self):
        self.player.score -= 1

    @update_display
    @update_score
    def score_plus(self):
        self.player.score += 1

    def load_player_data(self):
        pass
