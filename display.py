from PyQt5.QtWidgets import QMainWindow

from config import *

class Display_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "TI Scoreboard Display"
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)

    def update(self, players):
        pass
