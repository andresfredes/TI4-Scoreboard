from PyQt5.QtWidgets import QMainWindow

from config import WINDOW

class Display_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "TI Scoreboard Display"
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(
            WINDOW["XPOS"],
            WINDOW["YPOS"],
            WINDOW["WIDTH"],
            WINDOW["HEIGHT"]
        )

    def update(self, players):
        pass
