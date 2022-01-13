import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtCore


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("LoginWindow.ui", self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    # Clickable Buttons and Menus
        self.btnExit.clicked.connect(self.closeApplication)  # Exit Application
        self.btnLogin.clicked.connect(self.login)  # Login

    # Functions

    def closeApplication(self):
        QMainWindow.exec_()

    def login(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()

        if len(username) == 0:
            self.lblError.setText("Enter Username")
            self.txtUsername.setFocus()
        elif len(password) == 0:
            self.lblError.setText("Enter Password")
            self.txtPassword.setFocus()
        else:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            query = "SELECT password FROM users WHERE username ='%s'" % (
                username)
            cursor.execute(query)
            resultPass = cursor.fetchone()[0]
            if resultPass == password:
                conn.close()
                self.close()
            else:
                self.lblError.setText("Invalid Username or Password")
                self.lblError.adjustSize()
