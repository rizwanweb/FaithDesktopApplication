from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys

from login import LoginWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("UI/MainWindow.ui", self)
        self.showLogin()
    # Clickable Buttons and Menus

    # Functions

    def showLogin(self):
        self.loginWindow = LoginWindow()
        self.loginWindow.show()


# Main
app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.showMaximized()
try:
    sys.exit(app.exec_())
except:
    raise Exception
