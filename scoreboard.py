import sys

from gui import UI
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = UI()
    win.show()
    sys.exit(app.exec_())
