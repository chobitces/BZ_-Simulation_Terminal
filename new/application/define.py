

STR_COM_MSAREAD = "RDMSA reg len\r"
STR_COM_MSAWRITE = "WRMSA reg data\r"

STR_COM_RDOKSTING = "read ok!"
STR_COM_WROKSTING = "write ok!"

STR_1LN4_MSAREAD = "read_gui_msa_burst id,reg,len\r"
STR_1LN4_MSAWRITE = "write_gui_msa_burst id,reg,len\r"

STR_OTU4S_MSAREAD = "read_gui_msa_burst id,reg,len\r"
STR_OTU4S_MSAWRITE = "write_gui_msa_burst id,reg,len\r"

STR_1LN4_RDOKSTING = "func return value = 0x00000000"
STR_1LN4_WROKSTING = "func return value = 0x00000000"

STR_OTU4S_RDOKSTING = "value = 0 = 0x0"
STR_OTU4S_WROKSTING = "value = 0 = 0x0"

strTestBoardRead = "ReadCFP &pLaserChipOCH, "
strTestBoardWrite = "WriteCFP &pLaserChipOCH, "

#UPDATE_CMD = "download_cfp2_k10 id, filename\r"     #升级接口指令
UPDATE_CMD = "download_cfp2_k10 id"     #升级接口指令
logout_flag = "Connection closed by foreign host"     #长时间未操作，自动退出登录
