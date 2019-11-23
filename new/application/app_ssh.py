import threading, paramiko, sys
from PyQt5.QtCore import pyqtSignal
import time

loginSuccess = "-> "     #telnet登录成功返回该字符串

class SSH_Client:
    shell = None
    client = None
    transport = None

    def __init__(self):
        pass

    def sshclient_connectReadbackAck(self):
        '''
        函数名称：
        功    能：通过读取打印信息确认登录成功
        输    入：
        输    出：无
        说    明：
        :return:无
         '''

        try:
            #print("sshclient_connectReadbackAck")
            second_bak = time.time()  #获取系统时间（s）
            #print("get time")
            while (1):
                bytes = self.sshclient_rev()
                #print("bytes:",bytes)
                second_now = time.time()  #获取系统时间（s）
                if second_now - second_bak > 10:  #超时10s退出
                    print("connect timeout")
                    return -1

                if loginSuccess in bytes:
                    print("connect success")
                    break
                time.sleep(0.01)

            return 0
        except Exception as e:
            ctypes.windll.user32.MessageBoxA(0, u"连接未成功".encode('gb2312'), u'警告'.encode('gb2312'), 0)
            # print(e)

    def sshclient_connect(self,hostip,username,password,port):
        print("Connect to server", str(hostip) + ".")
        try:
            self.client = paramiko.client.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
            self.client.connect(hostip, username=username, password=password, look_for_keys=False, timeout=30)
            self.transport = paramiko.Transport((hostip, port))
            self.transport.banner_timeout = 30
            self.transport.connect(username=username, password=password)

            self.openShell()
            # self.sshclient_send("telnet " + ip + " " + port + "\r")
            # result = self.sshclient_connectReadbackAck()
            return 0
        except:
            print("connect error")
            return -1


    def closeConnection(self):
        if (self.client != None):
            self.client.close()
            self.transport.close()

    def openShell(self):
        self.shell = self.client.invoke_shell()

    def sshclient_send(self, command):
        if (self.shell):
            self.shell.send(command)
        else:
            print("Sesja nie otwarta.")

    def sshclient_rev(self):
        alldata = self.shell.recv(1024)

        if alldata:
            s = alldata.decode('utf-8',"ignore")
            s = s.replace('\r','')
            #print("s:",s)
        else:
            s = None
            #print("s is none")

        return s

    def sshclient_revready(self):
        return self.shell.recv_ready()





def printRev(str):
    print(str)



