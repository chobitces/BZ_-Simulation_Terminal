import paramiko
import os
import platform
import stat
import datetime

#hostip = '12.26.0.250'
#username = 'root'
#password = 'root'
#port = 22


# 格式化路径或拼接路径并格式化
def formatPath(path, *paths):
    """
    :param path: 路径1
    :param paths: 路径2-n
    :return:
    """
    if path is None or path == "." or path == "/" or path == "//":
        path = ""

    if len(paths) > 0:
        for pi in paths:
            if pi == "" or pi == ".":
                continue
            path = path + "/" + pi

    if path == "":
        return path

    while path.find("\\") >= 0:
        path = path.replace("\\", "/")
    while path.find("//") >= 0:
        path = path.replace("//", "/")

    if path.find(":/") > 0:  # 含磁盘符 NOT EQ ZERO, os.path.isabs NOT WORK
        if path.startswith("/"):
            path = path[1:]
    else:
        if not path.startswith("/"):
            path = "/" + path

    if os.path.isdir(path):  # remote path is not work
        if not path.endswith("/"):
            path = path + "/"
    elif os.path.isfile(path):  # remote path is not work
        if path.endswith("/"):
            path = path[:-1]
    elif path.find(".") < 0:  # maybe it is a dir
        if not path.endswith("/"):
            path = path + "/"
    else:  # maybe it is a file
        if path.endswith("/"):
            path = path[:-1]

    # print("new path is " + path)
    return path


# 上传指定文件
def uploadFile(sftp, remoteRelDir, localAbsPath):
    """
        函数名称：
        功    能：上传指定文件
        输    入：localAbsPath：电脑本地文件存放位置；remoteRelDir：目的路径
        输    出：无
        说    明：
        return  : 成功返回0;失败返回-1
        :param sftp:
        :param remoteRelDir: 服务端文件夹相对路径，可以为None、""，此时文件上传到homeDir
        :param localAbsPath: 客户端文件路径，当路径以localDir开始，文件保存到homeDir的相对路径下
        :return:
    """
    #print("start upload file by use SFTP...")
    try:
        try:
            sftp.chdir(remoteRelDir)
        except:
            try:
                sftp.mkdir(remoteRelDir)
            except:
                print("U have no authority to make dir")
                return -1

        fileName = os.path.basename(localAbsPath)
        remoteRelPath = formatPath(remoteRelDir, fileName)
        sftp.put(localAbsPath, remoteRelPath)
        return 0
    except Exception as e:
        print(4, e)
        return -1


#
def uploadDir(sftp, remoteRelDir, localAbsDir):
    """
          函数名称：
          功    能：上传指定文件夹下的所有,文件夹下无文件时,不上传；只有当文件夹不为空时,才会新建文件夹，并上传文件
          输    入：localAbsDir：电脑本地路径；remoteRelDir：目的路径
          输    出：无
          说    明：
          return  : 成功返回0;失败返回-1
        :param sftp:
        :param remoteRelDir: 服务端文件夹相对路径，可以为None、""，此时文件上传到homeDir
        :param localAbsDir: 客户端文件夹路径，当路径以localDir开始，文件保存到homeDir的相对路径下
        :return:
    """
    #print("start upload dir by use SFTP...")
    try:
        for root, dirs, files in os.walk(localAbsDir):
            if len(files) > 0:
                for fileName in files:
                    localAbsPath = formatPath(localAbsDir, fileName)
                    rs = uploadFile(sftp, remoteRelDir, localAbsPath)
                    if rs == -1:
                        return -1

            if len(dirs) > 0:
                for dirName in dirs:
                    rrd = formatPath(remoteRelDir, dirName)
                    lad = formatPath(localAbsDir, dirName)
                    rs = uploadDir(sftp, rrd, lad)
                    if rs == -1:
                        return -1
        return 0
    except Exception as e:
        print(3, e)
        return -1


def upload_bak(hostip, port, username, password, localAbsDir, remoteRelDir):
    '''
      函数名称：
      功    能：将本地路径localAbsDir下的文件夹及文件上传至remoteRelDir路径下
      输    入：localAbsDir：电脑本地路径；remoteRelDir：目的路径
      输    出：无
      说    明：
      return  : 成功返回0;失败返回-1
     '''
    try:
        t = paramiko.Transport((hostip, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)

        print('upload file start %s ' % datetime.datetime.now())
        try:
            #os.walk()返回结果是是一个元组，元组的第一个元素是输入的文件路径，第二个元素是当前路径下
            #所有的文件夹组成的列表，第三个元素是当前路径下所有文件组成的列表
            g = os.walk(localAbsDir)
            for root, dirs, files in g:
                if len(files) > 0:
                    for fileName in files:
                        localAbsPath = formatPath(localAbsDir, fileName)
                        rs = uploadFile(sftp, remoteRelDir, localAbsPath)
                        if rs == -1:
                            return -1
                if len(dirs) > 0:
                    for dirName in dirs:
                        rrd = formatPath(remoteRelDir, dirName)
                        lad = formatPath(localAbsDir, dirName)
                        rs = uploadDir(sftp, rrd, lad)
                        if rs == -1:
                            return -1
                break
            print('upload file success %s ' % datetime.datetime.now())
            t.close()
            return 0
        except Exception as e:
            print(1, e)
            return -1
    except Exception as e:
        print(2, e)
        return -1

def upload(hostip, port, username, password, localAbsPath, remoteRelDir):
    '''
      函数名称：
      功    能：将本地文件路径localAbsPath（指向某个具体文件）的文件上传至remoteRelDir（仅仅是路径）路径下
      输    入：localAbsPath：电脑本地文件存放位置；remoteRelDir：目的路径
      输    出：无
      说    明：
      return  : 成功返回0;失败返回-1
     '''
    try:
        t = paramiko.Transport((hostip, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)

        print('upload file start %s ' % datetime.datetime.now())
        try:
            rs = uploadFile(sftp, remoteRelDir, localAbsPath)
            if rs == -1:
                return -1
            print('upload file success %s ' % datetime.datetime.now())
            t.close()
            return 0
        except Exception as e:
            print(1, e)
            return -1
    except Exception as e:
        print(2, e)
        return -1

if __name__ == '__main__':
    localAbsDir = r"C:\Users\flp\Desktop\py_test\test"  # 本地需要上传的文件所处的目录
    remoteRelDir = r'\mnt\nandsim\run\WKE2202444R1B_OTN'  # linux下目录

    host_ip = '12.26.0.250'
    port = 22
    user_name = 'root'
    password = 'root'

    upload(host_ip, port, user_name, password,localAbsDir, remoteRelDir)
