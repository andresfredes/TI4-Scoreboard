from config import *
from PyQt5 import QtWidgets as QT
from PyQt5.QtWidgets import QMainWindow

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Twilight Imperium Scoreboard"
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self.xpos = WINDOW_XPOS
        self.ypos = WINDOW_YPOS
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.xpos, self.ypos, self.width, self.height)
        self.add_menu()

        self.show()

    def add_menu(self):
        menu = self.menuBar()

        file_menu = menu.addMenu('File')
        exit_option = QT.QAction('Exit', self)
        exit_option.setShortcut('Ctrl+Q')
        exit_option.setStatusTip('Exit Program')
        exit_option.triggered.connect(self.close)
        file_menu.addAction(exit_option)

    def close(self):
        print('Pax Magnifica Bellum Gloriosum')
        super().close()
