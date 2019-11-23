# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.selectwidget = QtWidgets.QWidget(self.centralwidget)
        self.selectwidget.setObjectName("selectwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.selectwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 5, 1, 1)
        self.connection_protocol = QtWidgets.QComboBox(self.selectwidget)
        self.connection_protocol.setMaximumSize(QtCore.QSize(100, 16777215))
        self.connection_protocol.setObjectName("connection_protocol")
        self.connection_protocol.addItem("")
        self.connection_protocol.addItem("")
        self.connection_protocol.addItem("")
        self.gridLayout.addWidget(self.connection_protocol, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.connection_protocol_label = QtWidgets.QLabel(self.selectwidget)
        self.connection_protocol_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.connection_protocol_label.setObjectName("connection_protocol_label")
        self.gridLayout.addWidget(self.connection_protocol_label, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 4, 1, 1)
        self.pushButton_ok = QtWidgets.QPushButton(self.selectwidget)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.gridLayout.addWidget(self.pushButton_ok, 1, 6, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 4, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 7, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.selectwidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 26))
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
        self.connection_protocol.setItemText(0, _translate("MainWindow", "serial"))
        self.connection_protocol.setItemText(1, _translate("MainWindow", "SSH"))
        self.connection_protocol.setItemText(2, _translate("MainWindow", "Telnet"))
        self.connection_protocol_label.setText(_translate("MainWindow", "协议"))
        self.pushButton_ok.setText(_translate("MainWindow", "确定"))

