import xlrd     #读取文件

#写入Excel文件,生成的文件后缀名为.xlsx，最大能够支持1048576行数据，16384列数据
import xlsxwriter
import configparser
import os


def read_data(str_filename):
    '''
    函数名称：
    功    能：读取.xls文件
    输    入：无
    输    出：无
    说    明：
    return  ： 成功返回0;失败返回-1
    '''
    # 打开excel文件读取数据
    exce = xlrd.open_workbook(str_filename)
    sheet1 = exce.sheet_by_name('Sheet1')  # 通过sheet名称获取

    #获取sheet1中行数和列数
    #nrows = sheet1.nrows
    #ncols = sheet1.ncols

    for rown in range(sheet1.nrows):
        rown_data = sheet1.row_values(rown)  # 通过下标获取某一行的数据

    for cown in range(sheet1.ncols):
        cown_data = sheet1.col_values(cown)  # 通过下标获取某一列的数据

    return 0

def write_data(str_filename, datalist):
    '''
    函数名称：
    功    能：向文件str_filename中写入列表datalist数据
    输    入：str_filename：字符串形式的文件名,可以是路径形式的； datalist数据列表
    输    出：无
    说    明：
    return  ：成功返回0;失败返回-1
    '''
    workbook = xlsxwriter.Workbook(str_filename)  # 创建一个excel文件
    worksheet = workbook.add_worksheet(u'sheet1')  # 在文件中创建一个名为sheet1的sheet,不加名字默认为sheet1

    headings = ['Hi', 'Hq', 'Vi', 'Vq']  # 设置表头
    worksheet.write_row('A1', headings)
    worksheet.write_column('A2', datalist[0])
    worksheet.write_column('B2', datalist[1])
    worksheet.write_column('C2', datalist[2])
    worksheet.write_column('D2', datalist[3])
    workbook.close()  # 将excel文件保存关闭，如果没有这一行运行代码会报错

    return 0


def read_cfgfile(str_cfgfilename):
    '''
      函数名称：
      功    能：读取.cfg文件,用于生成文件序号
      输    入：无
      输    出：无
      说    明：
      return  ： 成功返回待生成列表();失败返回-1
      '''
    try:
        file_name_list = []
        if os.path.exists(os.path.join(os.getcwd(), str_cfgfilename)):
            config = configparser.ConfigParser()
            config.read(str_cfgfilename)
            name = config.get("xls index", "file_name")
            index = config.get("xls index", "file_index")
            file_name_list.append(name)
            file_name_list.append(index)
            return file_name_list
        return -1
    except:
        return -1


def write_cfgfile(str_cfgfilename, str_fileNo):
    '''
     函数名称：
     功    能：写.cfg文件,用于生成文件序号
     输    入：str_cfgfilename:cfg文件; str_fileNo:文件名后的序号
     输    出：无
     说    明：
     return  ： 成功返回0;失败返回-1
     '''
    #if os.path.exists(os.path.join(os.getcwd(), str_filename)):
    conf = configparser.ConfigParser()
    cfgfile = open(str_cfgfilename, 'w')
    conf.add_section("xls index")  # 在配置文件中增加一个段

    str_filename = "collection"
    # 第一个参数是段名，第二个参数是选项名，第三个参数是选项对应的值
    conf.set("xls index", "file_name", str_filename)
    conf.set("xls index", "file_index", str_fileNo)
    conf.add_section("FL_Config")

    # 将conf对象中的数据写入到文件中
    conf.write(cfgfile)
    cfgfile.close()
    return 0


def creat_xls_file(datalist):
    '''
     函数名称：
     功    能：生成.xls文件
     输    入：datalist：待写入.xls文件的数据（数据类型为列表）
     输    出：无
     说    明：
     return  ： 成功返回0;失败返回-1
     '''
    str_cfgfilename = "index.cfg"
    filename_list = read_cfgfile(str_cfgfilename)   #从cfg文件中读取待写入文件的名字和序号
    if filename_list != -1:  #读取cfg索引文件失败
        str_filename = filename_list[0] + "_" + filename_list[1] + ".xls"
        write_data(str_filename, datalist)   #往.xls中写入数据

        str_fileNo = filename_list[1]   #文件末尾序号
        if (int(str_fileNo, 10) < 0) or (int(str_fileNo, 10) >= 19):  #最多创建20个文件
            str_fileNo = "0"
        else:
            temp = int(str_fileNo, 10) + 1
            str_fileNo = str(temp)
        write_cfgfile(str_cfgfilename, str_fileNo) #更新.cfg索引文件
        return 0
    else:
        str_filename = "collection_0.xls"
        write_data(str_filename, datalist)  # 往.xls中写入数据

        str_fileNo = "1"  # 文件末尾序号
        write_cfgfile(str_cfgfilename, str_fileNo)  # 更新.cfg索引文件
        return 0