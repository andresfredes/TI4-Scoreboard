from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QAction, QPushButton, QComboBox, QVBoxLayout,
    QLabel, QHBoxLayout, QFrame, QLineEdit, QSizePolicy)

from config import FACTIONS, COLOURS, STRAT_CARDS

class Font(QFont):
    def __init__(self):
        super().__init__()
        self.setPointSize(20)

class Label_Font(QFont):
    def __init__(self):
        super().__init__()
        self.setPointSize(40)

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
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(Label_Font())

class TextBox(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.setFont(Font())

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
        player_label = Label("Player " + str(self.player.num))
        vbox.addWidget(player_label)

        hbox1 = QHBoxLayout()
        self.player_name = TextBox()
        hbox1.addWidget(self.player_name)
        set_button = Button("Set Name", self.set_name)
        hbox1.addWidget(set_button)
        vbox.addLayout(hbox1)

        self.faction = ComboBox(FACTIONS, self.set_faction)
        vbox.addWidget(self.faction)

        self.colour = ComboBox(COLOURS.keys(), self.set_colour)
        vbox.addWidget(self.colour)

        self.strat_card = ComboBox(STRAT_CARDS.values(), self.set_strat_card)
        vbox.addWidget(self.strat_card)

        hbox2 = QHBoxLayout()
        self.used_button = Button("Card active", self.used_card_toggle)
        hbox2.addWidget(self.used_button)
        self.passed_button = Button("Player active", self.passed_toggle)
        hbox2.addWidget(self.passed_button)
        vbox.addLayout(hbox2)

        hbox3 = QHBoxLayout()
        minus_button = Button("-", self.score_minus)
        hbox3.addWidget(minus_button)
        self.score = Label(str(self.player.score))
        hbox3.addWidget(self.score)
        plus_button = Button("+", self.score_plus)
        hbox3.addWidget(plus_button)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)

    def update_display(func):
        def inner(self):
            func(self)
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
