# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_telnet.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        self.connection_connect_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connection_connect_button.sizePolicy().hasHeightForWidth())
        self.connection_connect_button.setSizePolicy(sizePolicy)
        self.connection_connect_button.setMinimumSize(QtCore.QSize(100, 50))
        self.connection_connect_button.setDefault(True)
        self.connection_connect_button.setObjectName("connection_connect_button")
        self.gridLayout.addWidget(self.connection_connect_button, 4, 1, 1, 2)
        self.comboBox_sshport = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_sshport.setEditable(True)
        self.comboBox_sshport.setObjectName("comboBox_sshport")
        self.comboBox_sshport.addItem("")
        self.gridLayout.addWidget(self.comboBox_sshport, 1, 2, 1, 2)
        self.comboBox_hostip = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_hostip.setEditable(True)
        self.comboBox_hostip.setObjectName("comboBox_hostip")
        self.comboBox_hostip.addItem("")
        self.comboBox_hostip.addItem("")
        self.comboBox_hostip.addItem("")
        self.gridLayout.addWidget(self.comboBox_hostip, 0, 2, 1, 2)
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 2, 2, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 26))
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
        self.label.setText(_translate("MainWindow", "主机名称"))
        self.label_2.setText(_translate("MainWindow", "端口"))
        self.label_5.setText(_translate("MainWindow", "会话名称"))
        self.connection_connect_button.setText(_translate("MainWindow", "Connect"))
        self.comboBox_sshport.setItemText(0, _translate("MainWindow", "23"))
        self.comboBox_hostip.setItemText(0, _translate("MainWindow", "10.18.1.45"))
        self.comboBox_hostip.setItemText(1, _translate("MainWindow", "10.26.0.250"))
        self.comboBox_hostip.setItemText(2, _translate("MainWindow", "12.26.0.250"))

