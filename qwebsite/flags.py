# Author: Acer Zhang
# Datetime: 2021/9/8 
# Copyright belongs to the author.
# Please indicate the source for reprinting.
import platform
import os
import sys

OS_FLAG_WINDOWS = "Windows"
OS_FLAG_MAC = "Darwin"
OS_FLAG_LINUX = "Linux"

OS_FLAG = platform.system()

if OS_FLAG == OS_FLAG_LINUX or OS_FLAG == OS_FLAG_MAC:
    HOSTS_FILE_PATH = "/etc/hosts"
else:
    try:
        import ctypes
    except Exception as e:
        print("当前操作系统安全策略无法使用ctypes模块，请安装杀毒软件修复系统漏洞进行解决，报错如下：", e)
        exit(1)
    # ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    HOSTS_FILE_PATH = os.path.join(os.environ["SYSTEMROOT"], "System32/drivers/etc/hosts")

ADD_FLAG = "ADD"
RESET_FLAG = "RESET"
