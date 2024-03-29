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

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import (QAction, QPushButton, QComboBox, QVBoxLayout,
    QLabel, QHBoxLayout, QFrame, QLineEdit, QSizePolicy)

from config import FACTIONS, COLOURS, LIGHT_COLOURS, STRAT_CARDS

class Font(QFont):
    def __init__(self, size=20):
        super().__init__()
        self.setPointSize(size)

class Action(QAction):
    def __init__(self, name, window, shortcut, tip, func):
        super().__init__(name, window)
        self.setShortcut(shortcut)
        self.setStatusTip(tip)
        self.triggered.connect(func)

class Button(QPushButton):
    def __init__(self, text, func):
        super().__init__()
        self.setText(text)
        self.clicked.connect(func)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.setFont(Font())

class ComboBox(QComboBox):
    def __init__(self, items, func):
        super().__init__()
        self.addItems(items)
        self.activated.connect(func)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.setFont(Font())

class Label(QLabel):
    def __init__(self, text="", size=40, style=None):
        super().__init__()
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
        font = Font(size)
        if style:
            if style == "strike":
                font.setStrikeOut(True)
            if style == "italic:":
                font.setItalic(True)
        self.setFont(font)

class TextBox(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.setFont(Font())

class Zero_Token(QPushButton):
    def __init__(self,  player):
        super().__init__()
        self.player = player
        self.setText("Naalu Zero Token")
        self.clicked.connect(self.changed)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setFont(Font())
        if self.player.is_zero:
            self.setIcon(QIcon('icons/checkmark.png'))
        
    def changed(self):
        if self.player.is_zero:
            self.player.is_zero = False
            self.setIcon(QIcon())
            btn_style = 'background-color: white'
        else:
            self.player.is_zero = True
            self.setIcon(QIcon('icons/checkmark.png'))
            btn_style = 'background-color: lightgray'
        self.setStyleSheet(btn_style)

class Player_Widget(QFrame):
    def __init__(self, player, display):
        super().__init__()
        self.player = player
        self.display = display
        self.init_UI()
        self.load_player_data()

    def init_UI(self):
        self.setLineWidth(1)
        self.setFrameShape(QFrame.StyledPanel)
        self.setStyleSheet('background-color: white')
        vbox = QVBoxLayout()

        if self.player.name == "":
            self.player_label = Label("Player " + str(self.player.num))
            vbox.addWidget(self.player_label)

            self.name_label = Label("Set Player Name", size=15)
            vbox.addWidget(self.name_label)

            self.hbox1 = QHBoxLayout()
            self.player_set_name = TextBox()
            self.hbox1.addWidget(self.player_set_name)
            self.set_button = Button("Set", self.set_name)
            self.hbox1.addWidget(self.set_button)
            vbox.addLayout(self.hbox1)
        else:
            self.player_label = Label(self.player.name)
            vbox.addWidget(self.player_label)

        self.faction = ComboBox(FACTIONS, self.set_faction)
        if self.player.faction:
            self.faction.setCurrentText(self.player.faction)
        vbox.addWidget(self.faction)

        self.colour = ComboBox(COLOURS.keys(), self.set_colour)
        if self.player.colour:
            self.colour.setCurrentText(self.player.colour)
        vbox.addWidget(self.colour)

        self.strat_card = ComboBox(STRAT_CARDS.values(), self.set_strat_card)
        if self.player.strat_card:
            for key, value in STRAT_CARDS.items():
                if value == self.player.strat_card:
                    self.strat_card.setCurrentText(STRAT_CARDS[key])
        vbox.addWidget(self.strat_card)

        vbox.addWidget(Zero_Token(self.player))

        hbox2 = QHBoxLayout()
        card_btn_label = Label("Card", size=15)
        hbox2.addWidget(card_btn_label)
        player_btn_label = Label("Player", size=15)
        hbox2.addWidget(player_btn_label)
        vbox.addLayout(hbox2)

        hbox3 = QHBoxLayout()
        btn_text = "Active"
        btn_style = 'background-color: white'
        if self.player.card_used:
            btn_text = "Used"
            btn_style = 'background-color: lightgray'
        self.used_button = Button(btn_text, self.used_card_toggle)
        self.used_button.setStyleSheet(btn_style)
        hbox3.addWidget(self.used_button)
        btn_text = "Active"
        btn_style = 'background-color: white'
        if self.player.passed:
            btn_text = "Used"
            btn_style = 'background-color: lightgray'
        self.passed_button = Button(btn_text, self.passed_toggle)
        self.passed_button.setStyleSheet(btn_style)
        hbox3.addWidget(self.passed_button)
        vbox.addLayout(hbox3)

        hbox4 = QHBoxLayout()
        minus_button = Button("-", self.score_minus)
        hbox4.addWidget(minus_button)
        self.score = Label(str(self.player.score))
        hbox4.addWidget(self.score)
        plus_button = Button("+", self.score_plus)
        hbox4.addWidget(plus_button)
        vbox.addLayout(hbox4)

        self.setLayout(vbox)

    def update_display(func):
        def inner(self):
            func(self)
            self.display.update()
        return inner

    @update_display
    def set_name(self):
        self.player_label.setText(self.player_set_name.text())
        self.player.name = self.player_set_name.text()
        self.hbox1.setParent(None)
        self.player_set_name.setParent(None)
        self.name_label.setParent(None)
        self.set_button.setParent(None)

    @update_display
    def set_faction(self):
        self.player.faction = self.faction.currentText()

    @update_display
    def set_colour(self):
        self.player.colour = self.colour.currentText()

    @update_display
    def set_strat_card(self):
        for key, value in STRAT_CARDS.items():
            if value == self.strat_card.currentText():
                self.player.strat_card = key

    @update_display
    def used_card_toggle(self):
        if self.player.card_used:
            self.used_button.setText("Active")
            self.used_button.setStyleSheet('background-color: white')
            self.player.card_used = False
        else:
            self.used_button.setText("Used")
            self.used_button.setStyleSheet('background-color: lightgray')
            self.player.card_used = True

    @update_display
    def passed_toggle(self):
        if self.player.passed:
            self.passed_button.setText("Active")
            self.passed_button.setStyleSheet('background-color: white')
            self.player.passed = False
        else:
            self.passed_button.setText("Passed")
            self.passed_button.setStyleSheet('background-color: lightgray')
            self.player.passed = True

    def update_score(func):
        def inner(self):
            func(self)
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

class Display_Widget(QFrame):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.init_UI()

    def init_UI(self):
        if self.player.is_turn:
            self.setLineWidth(15)
        else:
            self.setLineWidth(1)
        self.setFrameShape(QFrame.Box)
        foreground = ""
        if self.player.colour not in LIGHT_COLOURS:
            foreground = "; color:white;"
        self.setStyleSheet(
            'background-color: ' + COLOURS[self.player.colour] + foreground
        )

        vbox = QVBoxLayout()

        name = Label(self.player.name)
        vbox.addWidget(name)

        logo = QPixmap()
        folder = "icons/"
        if self.player.faction:
            suffix = ".png"
            logo.load(folder + self.player.faction + suffix)
        else:
            logo.load(folder + "TI.jpeg")
        logo_label = QLabel()
        logo_label.setPixmap(logo)
        logo_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        vbox.addWidget(logo_label, alignment=Qt.AlignCenter)

        strat_style = None
        if self.player.card_used:
            strat_style = "strike"
        strat_card = Label(
            STRAT_CARDS[self.player.strat_card],
            size = 30,
            style=strat_style)
        vbox.addWidget(strat_card)

        passed = Label("Passed")
        style_text = "color:" + COLOURS[self.player.colour]
        if self.player.passed:
            if self.player.colour not in LIGHT_COLOURS:
                style_text = "color:white"
            else:
                style_text = "color:black"
        passed.setStyleSheet(style_text)
        vbox.addWidget(passed)

        score = Label(str(self.player.score), size=100)
        vbox.addWidget(score)

        self.setLayout(vbox)
