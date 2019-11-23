import ctypes,threading
import time
import queue
from application.app_ssh import SSH_Client
from application.serialInterface import SerialInterface
from application.telnetcommand import TelnetClient





class Connection():

    def __init__(self):
        self.data_queue = queue.Queue(maxsize=1000)
        self.__clsInit()
        self.ConnectedFlag = 0
        self.RevFlag = 0
        self.readbuff = ""


    def __clsInit(self):
        self.ssh = SSH_Client()
        self.com = SerialInterface()
        self.net = TelnetClient()

    def apiLogin(self, paradict):
        result = 0
        print(paradict)
        if paradict["conntype"] =="serial":
            result = self.com.open(baudrate=paradict["baudrate"], port=paradict["comport"])
            self.logout = self.com.closeCom
            self.read = self.com.readLineData
            self.write = self.com.writedata
        elif paradict["conntype"] =="SSH":
            result = self.ssh.sshclient_connect(hostip = paradict["host_ip"],
                                                username = paradict["username"],
                                                password = paradict["userpassword"],
                                                port = int(paradict["ssh_port"]))
            self.logout = self.ssh.closeConnection
            self.read = self.ssh.sshclient_rev
            self.write = self.ssh.sshclient_send
        elif paradict["conntype"] =="Telnet":
            result = self.net.login_host(ip = paradict["host_ip"],port = int(paradict["ssh_port"]))
            self.logout = self.net.logout_host
            self.read = self.net.readData
            self.write = self.net.sendData
        else:
            ctypes.windll.user32.MessageBoxA(0, u"选择连接方式失败".encode('gb2312'), u' 错误'.encode('gb2312'), 0)

        if (0 == result):
            self.ConnectedFlag = 1
            print("connect success")
            self.receiveProcess = threading.Thread(target=self.__revDataProcess)
            self.receiveProcess.setDaemon(True)
            self.receiveProcess.start()


        return result

    def __revDataProcess(self):
        '''
        函数名称：
        功    能：接收数据，并触发数据上传，登录后创创建此线程
        输    入：无
        输    出：无
        说    明：
        :return:无
        '''
        while (self.ConnectedFlag == 1):
            try:
                bytes = self.read()
                if bytes != "":
                    self.data_queue.put(bytes)
                    # print("bytes:",bytes,end=""),
                    if self.RevFlag == 1:
                        self.readbuff = self.readbuff + bytes
                time.sleep(0.01)
            except:
                time.sleep(0.1)
                if(self.ConnectedFlag == 1):
                    ctypes.windll.user32.MessageBoxA(0, u"读取数据失败".encode('gb2312'), u' 警告'.encode('gb2312'), 0)
                else:
                    print("已退出")

    def sendcmd(self, sendstring, waitforstring):
        if self.ConnectedFlag == 1:
            self.write(sendstring)
            self.readbuff = ""
            self.RevFlag = 1
            second_bak = time.time()  # 获取当前系统时间秒数
            while 1:
                readbuf = self.readbuff.replace('\r', '')
                readbufflist = readbuf.split("\n")

                second_now = time.time()  # 获取当前系统时间秒数
                if second_now - second_bak > 5:  # 超时5秒退出
                    break
                if(waitforstring == ""):
                    break
                else:
                    if waitforstring in readbufflist:
                        break
                time.sleep(0.01)  # 这里加延时 防止跑死

            self.revFlag = 0
            return readbuf
        else:
            ctypes.windll.user32.MessageBoxA(0, u"未连接".encode('gb2312'), u' 警告'.encode('gb2312'), 0)
            return -1

    def MessageBox(self,tpstring):
        ctypes.windll.user32.MessageBoxA(0, tpstring.encode('gb2312'), u'信息'.encode('gb2312'), 0)




