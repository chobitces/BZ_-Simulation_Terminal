import serial
import serial.tools.list_ports
from time import sleep
import binascii

class SerialInterface():
    def __init__(self):
        self.com = serial.Serial()



    # 打开串口
    def open(self,baudrate = 115200,port = "COM13",bytesize = 8,parity = 'N',stopbits = 1,timeout = None,rts = False,dtr = False):
        self.com.baudrate = baudrate     #波特率
        self.com.port = port         #串口号
        self.com.bytesize = bytesize     #数据位数
        self.com.parity = parity       #校验位
        self.com.stopbits = stopbits     #停止位
        self.com.timeout = timeout      #超时等待时间
        self.com.rts = rts              #RTS
        self.com.dtr = dtr          #DTR
        if self.com.is_open:#如果串口已经打开
            print('Com is Opening')
            return -1
            pass
        else:
            try:
                self.com.open()
                print('Com is Opened')
            except:
                print('Com is error')
                return -1
        return 0

    #关闭串口
    def closeCom(self):
        if self.com.is_open:#如果串口已经打开
            self.com.close()
            #print('closed')
        else:
            pass

    # 发送一个字节
    def writedata(self,data,isHex=False):
        if isHex:
            data = binascii.unhexlify(data)
        # self.com.write(data.encode('utf-8'))
        self.com.write(data.encode('utf-8'))
        #print(data)

    #读数据
    def readdata(self):
        #n = self.ser.inWaiting()
        n = max(1, min(2048, self.com.in_waiting))
        if n:
            s = self.com.read(n)
            s = s.decode('utf-8',"ignore")
            #print(s,end="")   #bytes转字符串  # 第一参数默认utf8，第二参数默认strict
            s = s.replace('\r','')
            return s

    def readLineData(self):
        s = self.com.readline()
        if s:
            s = s.decode('utf-8',"ignore")
            s = s.replace('\r','')
        return s

    def findSerialPort(self):
        self.port_list = list(serial.tools.list_ports.comports())
        return self.port_list


def main():
    si = SerialInterface()
    portList = si.findSerialPort()
    if len(portList) == 0:
        print('找不到串口')
    else:
        for i in range(0, len(portList)):
            print(portList[i])

    si.open(baudrate = 115200,port = "COM4")

    while(1):
        receive = si.readLineData()
        if receive:
            print(receive,end = "")


# Call main when run as script
if __name__ == '__main__':
    main()

    

