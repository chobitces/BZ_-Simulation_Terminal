import application.define as Define
import ctypes
import inspect

"""
数据处理的包
"""
class DataHandle():
    def __init__(self):
        pass



    def check_ip(self,ipAddr):
        """
        检查IP是否正确
        :return:
        """
        addr=ipAddr.strip().split('.') #切割IP地址为一个列表
        #print addr
        if len(addr) != 4: #切割后列表必须有4个参数
            print("check ip address failed!")
            return False
        for i in range(4):
            try:
                addr[i]=int(addr[i]) #每个参数必须为数字，否则校验失败
            except:
                print ("check ip address failed!")
                return False
            if addr[i]<=255 and addr[i]>=0:  #每个参数值必须在0-255之间
                pass
            else:
                print("check ip address failed!")
                return False
            i+=1
        else:
            print("check ip address success!")
            return True


def addZero(strNum,bit):
    strNeed = ""
    lenth = len(strNum)
    # print(lenth)
    nbit = bit - lenth
    if lenth < bit:
        for i in range(0,nbit):
            strNeed = "0" + strNeed
    strReturn = strNeed + strNum
    # print(strReturn)
    return strReturn

def binStrToHexStr(strBin):
    """
    二进制字符串转化为16进制字符串
    :param strBin:输入的二进制数
    :return:输出的16进制数
    """
    intBin = int(strBin,2)
    strHex = hex(intBin).replace("L","")
    #print(strHex)
    return strHex

def hexStrToBinStr(numhex,bit):
    """
    将16进制数转化为2进制字符串
    :param numhex:输入的16进制数，以16进制字符串
    :param bit:输出2进制的位数
    :return:bit位的2进制数
    """
    intInt = int(numhex,16)
    strBin = bin(intInt).split("0b")[-1]
    strBin = addZero(strBin, bit)
    # print(strBin)
    return strBin


def dataHexToBitStr(numhex,bit):
    """
    将16进制字符串转化为按bit位的列表
    :param numhex:输入的16进制字符串
    :param bit:输出2进制的位数
    :return:按bit位排列的列表，BitStr[0]表示bit0
    """
    binstr = hexStrToBinStr(numhex,bit)
    # print(binstr)
    bitstr = binstr[::-1]
    # print(bitstr)
    return bitstr

def setHexBit(numhex,bit,data):
    """
    设置16进制数numhex 第bit位为 data
    :param numhex:输入的16进制数
    :param bit:改变第几位
    :param data:需要设置的值
    :return:修改后的值
    """
    if(data != 0 and data != 1):
        return -1

    # print(numhex)
    binstr = hexStrToBinStr(numhex, 16)
    # print(binstr)
    binstrlist = list(binstr)
    binstrlist[15 - bit] = str(data)
    binstr = "".join(binstrlist)
    # print(binstr)
    strhex = binStrToHexStr(binstr)
    # print(strhex)
    return strhex





def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


if __name__ == '__main__':
    ip = "10.26.0.0"
    if check_ip(ip) == True:
        print("IP is OK")
    else:
        print(ip + " is not IP")