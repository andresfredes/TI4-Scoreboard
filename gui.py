from PyQt5 import QtWidgets as QT
from PyQt5.QtWidgets import QMainWindow
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
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.xpos, self.ypos, self.width, self.height)
        self.add_menu()

    def add_menu(self):
        menu = self.menuBar()

        file_menu = menu.addMenu('File')
        exit_option = QT.QAction('Exit', self)
        exit_option.setShortcut('Ctrl+Q')
        exit_option.setStatusTip('Exit Program')
        exit_option.triggered.connect(self.close)
        file_menu.addAction(exit_option)

        display_menu = menu.addMenu('Display')
        add_option = QT.QAction('Open Scoreboard Display', self)
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
