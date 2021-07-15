from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout

from config import WINDOW
from custom_widgets import Display_Widget

class Display_Window(QMainWindow):
    def __init__(self, control_window):
        super().__init__()
        self.title = "TI Scoreboard Display"
        self.control_window = control_window
        self.players = []
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(
            WINDOW["XPOS"],
            WINDOW["YPOS"],
            WINDOW["WIDTH"],
            WINDOW["HEIGHT"]
        )
        self.setStyleSheet('background-color: darkgray')

    def update(self):
        if self.players:
            self.central_widget.setParent(None)
        if not self.control_window.players:
            return
        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout()
        self.players = sorted(
            self.control_window.get_players(),
            key=lambda x: x.strat_card
        )
        for player in self.players:
            player.widget = Display_Widget(player)
            self.central_layout.addWidget(player.widget)
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)
