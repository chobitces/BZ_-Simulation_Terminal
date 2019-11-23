import telnetlib
import time
import ctypes


class TelnetClient():
    def __init__(self,):
        self.tn = telnetlib.Telnet()

    # 此函数实现telnet登录主机
    def login_host(self,ip,port):
        try:
            print(ip,port)
            self.tn.open(host = ip,port = port)
        except:
            print('%s网络连接失败'%ip)
            ctypes.windll.user32.MessageBoxA(0, u"网络连接失败".encode('gb2312'), u' 警告'.encode('gb2312'), 0)
            return -1
        return 0
    # 此函数实现执行传过来的命令，并输出其执行结果
    def execute_some_command(self,command):
        # 执行命令
        self.tn.write(command.encode('ascii')+b'\n')
        time.sleep(2)
        # 获取命令结果
        command_result = self.tn.read_very_eager().decode('ascii')
        print('命令执行结果：\n%s' %command_result)

    def sendData(self,data):
        senddata = data.encode('ascii')
        # print(senddata)
        # self.tn.write(senddata)
        self.tn.write(senddata)


    def readData(self):
        strresult = self.tn.read_very_eager().decode('ascii')
        # strresult = self.tn.read_until("->",timeout=10)
        # print("R：" + strresult)
        return strresult

    # 退出telnet
    def logout_host(self):
        self.tn.write(b"exit\n")

if __name__ == '__main__':
    host_ip = '10.26.0.222'
    username = 'bmu852'
    password = 'aaaabbbb'
    command = ''
    telnet_client = TelnetClient()
    # 如果登录结果返加True，则执行命令，然后退出
    if telnet_client.login_host(host_ip,username,password):
        telnet_client.execute_some_command(command)
        telnet_client.logout_host()