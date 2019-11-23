"""
文 件 名:f_windows.py
作    者:byc
创建日期:2019年11月20日
文件描述:gui界面服务函数
版权说明:Copyright (c) 2000-2020   烽火通信科技股份有限公司
其    他:
修改日志:
"""




import sys,random
import windows.mainwindows
import windows.select
import windows.setting_serial
import windows.setting_ssh
import windows.setting_telnet
import windows.connectwindows
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import Qt


class SettingSerialWindows(QMainWindow, windows.setting_serial.Ui_MainWindow):
    def __init__(self):
        super(SettingSerialWindows, self).__init__()
        self.setupUi(self)

class SettingSSHWindows(QMainWindow, windows.setting_ssh.Ui_MainWindow):
    def __init__(self):
        super(SettingSSHWindows, self).__init__()
        self.setupUi(self)


class SettingTelnetWindows(QMainWindow, windows.setting_telnet.Ui_MainWindow):
    def __init__(self):
        super(SettingTelnetWindows, self).__init__()
        self.setupUi(self)


class Selectwindows(QMainWindow, windows.select.Ui_MainWindow):
    def __init__(self):
        super(Selectwindows, self).__init__()
        self.setupUi(self)

class ConnectWindows(QMainWindow, windows.connectwindows.Ui_MainWindow):
    def __init__(self):
        super(ConnectWindows, self).__init__()
        self.setupUi(self)

    def CreateSections(self, sections):
        for tp in range(len(sections)):
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
            self.treeWidget.topLevelItem(tp).setText(0, QtCore.QCoreApplication.translate("MainWindow", sections[tp]))



class MainGuiWindow(QMainWindow, windows.mainwindows.Ui_MainWindow):
    upkeypressflag = 0
    downkeypressflag = 0
    def __init__(self):
        super(MainGuiWindow, self).__init__()
        self.setupUi(self)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtCore.QCoreApplication.translate("MainWindow", "未连接"))

    def CreateTab(self,name):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtCore.QCoreApplication.translate("MainWindow", name))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.upkeypressflag = 1
        if event.key() == Qt.Key_Down:
            self.downkeypressflag = 1







def main_com():
    '''
    函数名称：main_com
    功    能：界面显示测试函数
    输    入：无
    输    出：无
    说    明：
    :return:
    '''
    app = QApplication(sys.argv)
    MainWindow = MainGuiWindow()
    #MainWindow = Selectwindows()
    MainWindow.show()
    sys.exit(app.exec_())

def test_connect():
    tplist = ["SSH1","SSH2","SSH3"]
    app = QApplication(sys.argv)
    MainWindow = ConnectWindows()
    MainWindow.show()
    MainWindow.CreateSections(tplist)
    sys.exit(app.exec_())


if __name__ == '__main__':
    #main_com()
    test_connect()