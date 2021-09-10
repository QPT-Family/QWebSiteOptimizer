import socket
import time
import sys

import ping3

from qwebsite.flags import *


def get_active_ip(host="github.com"):
    ips = list()
    try:
        result = socket.getaddrinfo(host, None, socket.AddressFamily.AF_INET, socket.SOCK_STREAM)
    except socket.gaierror:
        return ips

    for item in result:
        ip = item[4][0]
        ping_time = ping3.ping(ip, timeout=4, unit='ms')
        if ping_time:
            ips.append((ip, ping_time))
    ips_sort = sorted(ips, key=lambda x: x[1])
    return ips_sort


class EditHost:
    def __init__(self, hosts_file_path=None):
        if hosts_file_path is None:
            hosts_file_path = HOSTS_FILE_PATH
        self.hosts_file_path = hosts_file_path
        # 记录额外信息
        self.hosts_data = list()
        self.hosts_data_end = list()
        # 记录KV 地址-IP
        self.host_kv = dict()
        self._update()

    def add_data(self, ip, address):
        self.host_kv[address] = ip

    def del_data(self, address):
        if address in self.host_kv:
            self.host_kv.pop(address)

    def _update(self):
        self.hosts_data = list()
        self.host_kv = dict()
        with open(self.hosts_file_path, "r") as f:
            hosts_data = f.readlines()
        for line_ori in hosts_data:
            line = line_ori.strip("\n").split("\t")
            if len(line) == 2:
                self.host_kv[line[1]] = line[0]
            elif not line[0]:
                continue
            elif line[0][0] == "#":
                self.hosts_data.append(line[0] + "\n")
            else:
                self.hosts_data.append(line_ori)

    def write(self, out_dir=None):
        if not out_dir:
            out_dir = self.hosts_file_path
        pre_data = self.hosts_data.copy()
        for k, v in self.host_kv.items():
            line = f"{v}\t{k}\n"
            pre_data.append(line)
        with open(out_dir, "w") as f:
            f.writelines(pre_data + self.hosts_data_end)
        self._update()


class BaseOptimizer:
    def __init__(self, urls, mode=ADD_FLAG):
        if OS_FLAG == OS_FLAG_WINDOWS:
            try:
                import ctypes
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            except Exception as e:
                print("当前操作系统安全策略无法使用ctypes模块，请安装杀毒软件修复系统漏洞进行解决，报错如下：", e)
                exit(1)
        self.urls = urls
        self.ed = EditHost()
        self.mode = mode
        self._make()

    def _make(self):
        if self.mode == RESET_FLAG:
            for url in self.urls:
                self.ed.del_data(url)
        else:
            os.popen('ipconfig /flushdns')
            for url in self.urls:
                for i in range(2):
                    ip_info = get_active_ip(url)
                    if ip_info:
                        ip, ms = ip_info[0]
                        print(f"Info:\t{url}\t匹配到最快路径，延时为{ms:.4f}ms")
                        self.ed.add_data(ip, url)
                        break
                    else:
                        print(f"\r正在尝试重连...第{i + 1}次", flush=True, end="")
                        time.sleep(3)
                else:
                    print(f"\r\033[33mWarning:\t{url}\t中未搜索到可用IP，可能由于政策与法规限制，也可能是您的DNS出现了问题，"
                          f"可尝试修改本地网络DNS设置来解决非政策引起的搜索失败问题。\033[0m")
        self.ed.write()


class GitHubOptimizer(BaseOptimizer):
    def __init__(self, mode=ADD_FLAG):
        # 此处URL来源整理自 GitHub:521xueweihan/GitHub520
        urls = ["alive.github.com",
                "live.github.com",
                "github.githubassets.com",
                "central.github.com",
                "desktop.githubusercontent.com",
                "assets-cdn.github.com",
                "camo.githubusercontent.com",
                "github.map.fastly.net",
                "github.global.ssl.fastly.net",
                "gist.github.com",
                "github.io",
                "github.com",
                "github.blog",
                "api.github.com",
                "raw.githubusercontent.com",
                "user-images.githubusercontent.com",
                "favicons.githubusercontent.com",
                "avatars5.githubusercontent.com",
                "avatars4.githubusercontent.com",
                "avatars3.githubusercontent.com",
                "avatars2.githubusercontent.com",
                "avatars1.githubusercontent.com",
                "avatars0.githubusercontent.com",
                "avatars.githubusercontent.com",
                "github-cloud.s3.amazonaws.com",
                "github-com.s3.amazonaws.com",
                "github-production-release-asset-2e65be.s3.amazonaws.com",
                "github-production-user-asset-6210df.s3.amazonaws.com",
                "github-production-repository-file-5c1aeb.s3.amazonaws.com",
                "githubstatus.com",
                "github.community",
                "media.githubusercontent.com"]
        super(GitHubOptimizer, self).__init__(urls, mode)


if __name__ == '__main__':
    # print(get_active_ip("www.baidu.com"))

    # _ed = EditHost()
    # _url = "www.baidu.com"
    # _tmp = get_active_ip("www.baidu.com")[0][0]
    # _ed.add_data(_tmp, _url)
    # _ed.write("./test.txt")
    GitHubOptimizer()
    # https://www.cnblogs.com/nicholas-920610/articles/7149057.html