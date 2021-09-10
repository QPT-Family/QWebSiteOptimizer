# Author: Acer Zhang
# Datetime: 2021/9/8 
# Copyright belongs to the author.
# Please indicate the source for reprinting.
import platform
import os

OS_FLAG_WINDOWS = "Windows"
OS_FLAG_MAC = "Darwin"
OS_FLAG_LINUX = "Linux"

OS_FLAG = platform.system()

HOSTS_FILE_PATH = None


if OS_FLAG == OS_FLAG_LINUX or OS_FLAG == OS_FLAG_MAC:
    HOSTS_FILE_PATH = "/etc/hosts"
else:
    HOSTS_FILE_PATH = os.path.join(os.environ["SYSTEMROOT"], "System32/drivers/etc/hosts")


ADD_FLAG = "ADD"
RESET_FLAG = "RESET"
