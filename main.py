from select import select
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys

from login import LoginWindow
from chartOfAccounts import AccountWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("UI/MainWindow.ui", self)
        #self.showLogin()
    # Clickable Buttons and Menus

        self.actionChartOfAccounts.triggered.connect(self.openChartOfAccounts) #Open Chart of Accounts

    # Functions



    def openChartOfAccounts(self):
        self.accountWindow = AccountWindow()
        self.accountWindow.show()

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
