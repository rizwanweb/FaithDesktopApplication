import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore


class Dashboard(QDialog):
    def __init__(self):
        super(Dashboard, self).__init__()
        loadUi("UI/Dashboard.ui", self)
        #self.setWindowModality(QtCore.Qt.ApplicationModal)
        

        # Button Clicks


    # Functions


    
    
    #Database Connection function
    def connect(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        return cursor, conn
