from PyQt5.QtWidgets import (QMainWindow, QAction, QWidget, QPushButton,
    QHBoxLayout, QSizePolicy)

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
        self.players = {}
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.xpos, self.ypos, self.width, self.height)
        self.add_menu()
        self.refresh()

    def add_player(self):
        player_num = len(self.players) + 1
        self.players[str(player_num)] = Player_Widget(player_num)
        self.refresh()

    def refresh(self):
        if self.players:
            tmp_players = self.players.copy() #------------------------------------
            self.central_widget.setParent(None)
            self.players = tmp_players.copy() #-------------------------------------
        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout()
        if self.players:
            for player in self.players:
                self.central_layout.addWidget(self.players[player]) #----------------
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
        print("Opening display")
        self.display = Display_Window()
        self.display.show()

    def close(self):
        super().close()

class Player_Widget(QWidget):
    def __init__(self, player_num):
        super().__init__()
        self.player_num = player_num
