import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.uic import loadUi
from PyQt5 import QtCore


class AccountWindow(QMainWindow):
    def __init__(self):
        super(AccountWindow, self).__init__()
        loadUi("UI/AccountWindow.ui", self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.populateList()  # Populate List at open

        # Button Clicks
        self.btnExit.clicked.connect(self.closeWindow)  # Close Window
        self.btnNew.clicked.connect(self.clearedit)  # Clear all text area
        self.btnSave.clicked.connect(self.saveClient)  # Save Client
        self.listView.itemClicked.connect(self.selectedClient)  # Populate form
        self.btnDelete.clicked.connect(self.deleteClient)

    # Functions


    def deleteClient(self):
        cursor, conn = self.connect()
        query = "DELETE FROM clients WHERE companyName='%s'" % (
            self.listView.item(self.listView.currentRow()).text())
        cursor.execute(query)
        conn.commit()
        self.listView.clear()
        self.populateList()
        self.clearedit()

    def selectedClient(self):
        cursor, conn = self.connect()
        query = "SELECT * FROM clients WHERE companyName='%s'" % (
            self.listView.item(self.listView.currentRow()).text())
        cursor.execute(query)
        client = cursor.fetchone()
        self.txtCompanyName.setText(client[1])
        self.txtContactPerson.setText(client[2])
        self.txtMobile.setText(client[3])
        self.txtPhone.setText(client[4])
        self.txtEmail.setText(client[5])
        self.txtAddress.setText(client[6])
        self.txtCity.setText(client[7])
        self.txtNTN.setText(client[8])
        self.txtGST.setText(client[9])
        conn.close()

    def closeWindow(self):
        self.close()

    def clearedit(self):
        for child in self.findChildren(QLineEdit):
            child.clear()
            self.txtAddress.clear()
            self.txtCompanyName.setFocus()

    def saveClient(self):
        company = self.txtCompanyName.text().upper()
        person = self.txtContactPerson.text().upper()
        mobile = self.txtMobile.text()
        phone = self.txtPhone.text()
        email = self.txtEmail.text()
        address = self.txtAddress.toPlainText().upper()
        city = self.txtCity.text().upper()
        ntn = self.txtNTN.text()
        gst = self.txtGST.text()


        cursor, conn = self.connect()
        try:
            cursor.execute("REPLACE INTO clients(companyName, person, mobile, phone, email, address, city, ntn, gst) VALUES(?,?,?,?,?,?,?,?,?)",
                           (company, person, mobile, phone, email, address, city, ntn, gst))
            conn.commit()
            self.clearedit()
            self.listView.clear()
            self.populateList()
            conn.close()
        except sqlite3.IntegrityError as e:
            print(e)

    def populateList(self):
        cursor, conn = self.connect()
        query = "SELECT companyName FROM clients"
        try:
            cursor.execute(query)
            names = cursor.fetchall()
            conn.close()
            print(names)
            for client in names:
                self.listView.addItem(client[0])
        except sqlite3.IntegrityError as e:
            print(e)


    #Database Connection function
    def connect(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        return cursor, conn