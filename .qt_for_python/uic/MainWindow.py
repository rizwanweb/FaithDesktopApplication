# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/riz/Python/PYQT/Faith/UI/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Home = QtWidgets.QWidget(self.centralwidget)
        self.Home.setGeometry(QtCore.QRect(-1, -1, 801, 551))
        self.Home.setObjectName("Home")
        self.label = QtWidgets.QLabel(self.Home)
        self.label.setGeometry(QtCore.QRect(280, 16, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setMinimumSize(QtCore.QSize(0, 5))
        self.menubar.setSizeIncrement(QtCore.QSize(0, 10))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuActivities = QtWidgets.QMenu(self.menubar)
        self.menuActivities.setObjectName("menuActivities")
        self.menuBilling = QtWidgets.QMenu(self.menubar)
        self.menuBilling.setObjectName("menuBilling")
        self.menuReports = QtWidgets.QMenu(self.menubar)
        self.menuReports.setObjectName("menuReports")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCompanySetup = QtWidgets.QAction(MainWindow)
        self.actionCompanySetup.setObjectName("actionCompanySetup")
        self.actionDateSetup = QtWidgets.QAction(MainWindow)
        self.actionDateSetup.setObjectName("actionDateSetup")
        self.actionChartOfAccounts = QtWidgets.QAction(MainWindow)
        self.actionChartOfAccounts.setObjectName("actionChartOfAccounts")
        self.actionAdd_New_Job = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Job.setObjectName("actionAdd_New_Job")
        self.actionJob_List = QtWidgets.QAction(MainWindow)
        self.actionJob_List.setObjectName("actionJob_List")
        self.actionAdd_New_PID = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_PID.setObjectName("actionAdd_New_PID")
        self.actionPID_List = QtWidgets.QAction(MainWindow)
        self.actionPID_List.setObjectName("actionPID_List")
        self.actionCreate_New_Bill = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_Bill.setObjectName("actionCreate_New_Bill")
        self.actionCreate_New_PID_Bill = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_PID_Bill.setObjectName("actionCreate_New_PID_Bill")
        self.actionAdd_New_Item = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Item.setObjectName("actionAdd_New_Item")
        self.actionAdd_New_Terminal = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Terminal.setObjectName("actionAdd_New_Terminal")
        self.menuFile.addAction(self.actionCompanySetup)
        self.menuFile.addAction(self.actionDateSetup)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionChartOfAccounts)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAdd_New_Item)
        self.menuActivities.addAction(self.actionAdd_New_Job)
        self.menuActivities.addAction(self.actionJob_List)
        self.menuActivities.addSeparator()
        self.menuActivities.addAction(self.actionAdd_New_PID)
        self.menuActivities.addAction(self.actionPID_List)
        self.menuBilling.addAction(self.actionCreate_New_Bill)
        self.menuBilling.addSeparator()
        self.menuBilling.addAction(self.actionCreate_New_PID_Bill)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActivities.menuAction())
        self.menubar.addAction(self.menuBilling.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Faith Associates"))
        self.label.setText(_translate("MainWindow", "HOME"))
        self.menuFile.setTitle(_translate("MainWindow", "Accounts"))
        self.menuActivities.setTitle(_translate("MainWindow", "Activities"))
        self.menuBilling.setTitle(_translate("MainWindow", "Billing"))
        self.menuReports.setTitle(_translate("MainWindow", "Reports"))
        self.actionCompanySetup.setText(_translate("MainWindow", "Company Setup"))
        self.actionDateSetup.setText(_translate("MainWindow", "Date Setup"))
        self.actionChartOfAccounts.setText(_translate("MainWindow", "Chart Of Accounts"))
        self.actionAdd_New_Job.setText(_translate("MainWindow", "Add New Job"))
        self.actionJob_List.setText(_translate("MainWindow", "Job List"))
        self.actionAdd_New_PID.setText(_translate("MainWindow", "Add New PID"))
        self.actionPID_List.setText(_translate("MainWindow", "PID List"))
        self.actionCreate_New_Bill.setText(_translate("MainWindow", "Create New Bill"))
        self.actionCreate_New_PID_Bill.setText(_translate("MainWindow", "Create New PID Bill"))
        self.actionAdd_New_Item.setText(_translate("MainWindow", "Item Management"))
        self.actionAdd_New_Terminal.setText(_translate("MainWindow", "Add New Terminal"))
