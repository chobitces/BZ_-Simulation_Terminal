# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connectwindows.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 250))
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout.addWidget(self.treeWidget, 0, 1, 1, 1)
        self.pushButton_connect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_connect.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.gridLayout.addWidget(self.pushButton_connect, 3, 1, 1, 1)
        self.pushButton_creat = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_creat.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_creat.setObjectName("pushButton_creat")
        self.gridLayout.addWidget(self.pushButton_creat, 2, 1, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout.addWidget(self.pushButton_close, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "section"))
        self.pushButton_connect.setText(_translate("MainWindow", "连接"))
        self.pushButton_creat.setText(_translate("MainWindow", "新建"))
        self.pushButton_close.setText(_translate("MainWindow", "关闭"))

