import os
import sys
import ctypes
import re
import time
import threading

import application.tool as Tool

from application.config import Config
from application.serialInterface import SerialInterface
from application.connection import Connection
from PyQt5.QtCore import QObject,pyqtSignal
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtGui import QTextCursor
from windows.f_windows import MainGuiWindow,Selectwindows,SettingSerialWindows,\
                                SettingSSHWindows,ConnectWindows,SettingTelnetWindows



class Application(QObject):
    receiveUpdateSignal = pyqtSignal(str)   #定义信号,定义参数为str类型
    def __init__(self):
        super(Application, self).__init__()
        self.currentpath = os.getcwd()
        self.classinit()
        self.event_init()
        self.valueinit()
        self.MainWindow.show()
        self.sections = self.Config.read_section()
        self.process_init()
        if self.sections:
            self.ConnectWindow.show()
            self.ConnectWindow.CreateSections(self.sections)


    def classinit(self):
        self.com = SerialInterface()
        self.MainWindow = MainGuiWindow()
        self.SelectWindow = Selectwindows()
        self.ConnectWindow = ConnectWindows()
        self.ConnectApi = Connection()
        self.Config = Config(self.currentpath)





    def valueinit(self):
        self.connect_type = ""
        self.SettingWindow = None
        self.connectedFlag = 0
        self.sendbufflist = [""]
        self.currentbuffcnt = 0
    def event_init(self):
        self.receiveUpdateSignal.connect(self.updateReceivedDataDisplay)  # 绑定信号和槽函数
        self.MainWindow.action.triggered.connect(self.SelectWindow.show)
        self.MainWindow.action_runscript.triggered.connect(self.runscript)
        self.MainWindow.action_stopscript.triggered.connect(self.stopscript)
        self.MainWindow.lineEditSendAera.returnPressed.connect(self.sendDataFormSendArea)  #绑定打印窗口界面上的回车键为发送按钮
        self.SelectWindow.pushButton_ok.clicked.connect(self.get_connect_type_param)


        self.ConnectWindow.pushButton_creat.clicked.connect(self.SelectWindow.show)
        self.ConnectWindow.pushButton_connect.clicked.connect(self.sections_connect)
        self.ConnectWindow.pushButton_close.clicked.connect(self.ConnectWindow.close)




    def process_init(self):
        self.oneSecProcess = threading.Thread(target=self.oneSecondProcess)
        self.oneSecProcess.setDaemon(True)
        self.oneSecProcess.start()

    def runscript(self):
        file_dir = QFileDialog.getOpenFileName(None, '选择文件', '', 'Script Files(*.py)')
        str_dir = str(file_dir[0])  # 元组转字符串
        # print(str_dir)
        self.scriptPrcocess = threading.Thread(target=self.scriptPro,args=(str_dir,))
        self.scriptPrcocess.setDaemon(True)
        self.scriptPrcocess.start()


    def stopscript(self):
        Tool.stop_thread(self.scriptPrcocess)
        self.MainWindow.action_stopscript.setEnabled(False)
        self.MainWindow.action_runscript.setEnabled(True)

    def scriptPro(self,path):
        self.MainWindow.action_stopscript.setEnabled(True)
        self.MainWindow.action_runscript.setEnabled(False)
        import imp
        other = imp.load_source('script', path)
        try:
            other.main(self.ConnectApi)
        except Exception as e:
            print(e)
            self.MainWindow.action_stopscript.setEnabled(False)
            self.MainWindow.action_runscript.setEnabled(True)
            return

        self.MainWindow.action_stopscript.setEnabled(False)
        self.MainWindow.action_runscript.setEnabled(True)
        return






    def oneSecondProcess(self):
        while 1:
            if(self.MainWindow.upkeypressflag == 1):
                self.MainWindow.upkeypressflag = 0
                tplen = len(self.sendbufflist)
                print(tplen,self.currentbuffcnt)
                if(tplen > 0 and tplen > self.currentbuffcnt):
                    if(self.currentbuffcnt < tplen - 1):
                        self.currentbuffcnt = self.currentbuffcnt + 1
                        currentcmd = self.sendbufflist[tplen - self.currentbuffcnt]
                    else:
                        currentcmd = ""
                    self.MainWindow.lineEditSendAera.setText(currentcmd)

            if(self.MainWindow.downkeypressflag == 1):
                self.MainWindow.downkeypressflag = 0
                tplen = len(self.sendbufflist)
                print(tplen,self.currentbuffcnt)
                if(tplen > 0):
                    if(self.currentbuffcnt > 1):
                        self.currentbuffcnt = self.currentbuffcnt - 1
                        currentcmd = self.sendbufflist[tplen - self.currentbuffcnt]
                    else:
                        currentcmd = ""
                    self.MainWindow.lineEditSendAera.setText(currentcmd)



            time.sleep(0.1)
    def get_connect_type_param(self):
        """
        获取连接方式
        :return:
        """
        self.connect_type = self.SelectWindow.connection_protocol.currentText()
        self.SelectWindow.close()
        if self.connect_type == "serial":
            self.SettingWindow = SettingSerialWindows()
            portList = self.com.findSerialPort()
            if len(portList) > 0:
                for i in portList:
                    showStr = str(i[1])
                    self.SettingWindow.comboBox_port.addItem(showStr) #addItem()方法是添加一个选项
        elif self.connect_type == "SSH":
            self.SettingWindow = SettingSSHWindows()
            self.SettingWindow.lineEdit_name.setText(self.SettingWindow.comboBox_hostip.currentText())
        elif self.connect_type == "Telnet":
            self.SettingWindow = SettingTelnetWindows()
            self.SettingWindow.lineEdit_name.setText(self.SettingWindow.comboBox_hostip.currentText())
        else:
            ctypes.windll.user32.MessageBoxA(0, u"选择连接方式失败".encode('gb2312'), u' 错误'.encode('gb2312'), 0)

        self.SettingWindow.show()
        self.SettingWindow.connection_connect_button.clicked.connect(self.connection_connect)
    def connection_connect(self):
        tpdict = {}
        cnt = 0
        name = ""
        tpdict["conntype"] = self.connect_type
        if self.connect_type == "serial":
            resultlist = re.findall(r'[(](.*?)[)]',self.SettingWindow.comboBox_port.currentText(),re.S)
            tpdict["comport"] = resultlist[0]
            tpdict["baudrate"] = self.SettingWindow.comboBox_baudrate.currentText()
            tpdict["databit"] = self.SettingWindow.comboBox_databit.currentText()
            tpdict["parity"] = self.SettingWindow.comboBox_parity.currentText()
            tpdict["stopbits"] = self.SettingWindow.comboBox_stopbits.currentText()
            tpdict["name"] = tpdict["comport"]
        elif self.connect_type == "SSH":
            tpdict["host_ip"] = self.SettingWindow.comboBox_hostip.currentText()
            tpdict["ssh_port"] = self.SettingWindow.comboBox_sshport.currentText()
            tpdict["username"] = self.SettingWindow.lineEdit_username.text()
            tpdict["userpassword"] = self.SettingWindow.lineEdit_userpassword.text()
            tpdict["name"] = self.SettingWindow.lineEdit_name.text()
        elif self.connect_type == "Telnet":
            tpdict["host_ip"] = self.SettingWindow.comboBox_hostip.currentText()
            tpdict["ssh_port"] = self.SettingWindow.comboBox_sshport.currentText()
            tpdict["name"] = self.SettingWindow.lineEdit_name.text()
        else:
            ctypes.windll.user32.MessageBoxA(0, u"选择连接方式失败".encode('gb2312'), u' 错误'.encode('gb2312'), 0)

        result = self.ConnectApi.apiLogin(tpdict)
        if result == -1:
            ctypes.windll.user32.MessageBoxA(0, u"连接失败".encode('gb2312'), u' 警告'.encode('gb2312'), 0)
            return -1
        else:
            while 1:
                section = self.Config.read_section()
                if tpdict["name"] in section:
                    if "(" in tpdict["name"]:
                        tpdict["name"] = tpdict["name"].split("(")[0] + "(cnt)".replace("cnt",str(cnt))
                    else:
                        tpdict["name"] = tpdict["name"] + "(cnt)".replace("cnt",str(cnt))

                else:
                    break
                cnt = cnt + 1
            self.Config.save(tpdict)
            self.connectedFlag = 1
            self.receiveProcess = threading.Thread(target=self.revDataDiaplayProcess)
            self.receiveProcess.setDaemon(True)
            self.receiveProcess.start()
            self.SettingWindow.close()
            self.MainWindow.CreateTab(tpdict["name"])
    def sections_connect(self):
        tpdict = {}
        try:
            currentSection = self.ConnectWindow.treeWidget.selectedItems()[0].text(0)
            print(currentSection)
        except:
            ctypes.windll.user32.MessageBoxA(0, u"请选择Sessions".encode('gb2312'), u' 警告'.encode('gb2312'), 0)
            return -1
        tpdict = self.Config.load(currentSection)
        self.ConnectWindow.close()
        # print(tpdict)
        result = self.ConnectApi.apiLogin(tpdict)
        if result == -1:
            ctypes.windll.user32.MessageBoxA(0, u"连接失败".encode('gb2312'), u' 警告'.encode('gb2312'), 0)
        else:
            self.connectedFlag = 1
            self.receiveProcess = threading.Thread(target=self.revDataDiaplayProcess)
            self.receiveProcess.setDaemon(True)
            self.receiveProcess.start()
            self.MainWindow.CreateTab(currentSection)






    def revDataDiaplayProcess(self):
        while 1:
            if(self.connectedFlag == 1):
                s = self.ConnectApi.data_queue.get()
                self.receiveUpdateSignal.emit(s)    #触发信号：触发信息上传
            time.sleep(0.01)
    def updateReceivedDataDisplay(self, str):
        '''
        函数名称：
        功    能：将接收到的数据上传到打印显示区域，需要触发信号receiveUpdateSignal.emit触发后才会有数据
        输    入：接收到的数据
        输    出：无
        说    明：
        :return: 无
        '''
        if str != "":
            curScrollValue = self.MainWindow.textEditRevAera.verticalScrollBar().value()
            self.MainWindow.textEditRevAera.moveCursor(QTextCursor.End)
            endScrollValue = self.MainWindow.textEditRevAera.verticalScrollBar().value()
            self.MainWindow.textEditRevAera.insertPlainText(str)
            if curScrollValue < endScrollValue:
                self.MainWindow.textEditRevAera.verticalScrollBar().setValue(curScrollValue)
            else:
                self.MainWindow.textEditRevAera.moveCursor(QTextCursor.End)
    def sendDataFormSendArea(self):
        '''
        函数名称：
        功    能：打印显示窗口界面上，按回车键或者发送键发送待发送数据
        输    入：无
        输    出：无
        返 回 值：
        说    明：
        '''
        try:
            data = self.MainWindow.lineEditSendAera.text()
            data = data.replace("\n","") + "\n"
            if(data != "\n"):
                self.sendbufflist.append(data)
                self.currentbuffcnt = 0
            #print("print_window send:", data)
            self.ConnectApi.write(data)
            self.MainWindow.lineEditSendAera.clear()
            #self.receiveUpdateSignal.emit("")
        except Exception as e:
            print(e)


def main_com():
    '''
    函数名称：
    功    能：主函数
    输    入：无
    输    出：无
    返 回 值：
    说    明：
    '''
    app = QApplication(sys.argv)
    maincode = Application()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main_com()