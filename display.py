# Copyright 2021, Andres Fredes, <andres.hector.fredes@gmail.com>
# 
# This file is part of TI4-Scoreboard.
# 
#     TI4-Scoreboard is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     TI4-Scoreboard is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with TI4-Scoreboard.  If not, see <https://www.gnu.org/licenses/>.

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
            key=lambda x: (not x.is_zero, x.strat_card)
        )
        for player in self.players:
            player.widget = Display_Widget(player)
            self.central_layout.addWidget(player.widget)
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)
