# Author: Acer Zhang
# Datetime: 2021/9/28 
# Copyright belongs to the author.
# Please indicate the source for reprinting.
import os
import re
import requests

from qgui import CreateQGUI
from qgui.banner_tools import GitHub
from qgui.notebook_tools import *
from qwebsite.base import GitHubOptimizer
from qwebsite.flags import *

from qwebsite import __version__

ISO_LIST = ["https://hub.fastgit.org",
            "https://github.com.cnpmjs.org",
            "https://git.sdut.me",
            "https://github.wuyanzheshui.workers.dev"]


def set_iso(url):
    out = os.popen(f"git config --global url.{url}.insteadof https://github.com/").read()
    if out:
        print("执行情况如下：\n", out)


def ping_iso(url):
    print(f"开始测试{url}镜像源")
    try:
        ping_time = requests.get(url, timeout=4).elapsed.total_seconds()
        if ping_time < 1:
            print(f"镜像源\t{url}网络质量较好")
        elif ping_time < 2:
            print(f"镜像源\t{url}网络质量一般")
        else:
            print(f"镜像源\t{url}网络质量较差")
        print(f"镜像源\t{url}的响应时间为{ping_time:.4f}s")
    except requests.exceptions.ConnectTimeout:
        print(f"镜像源\t{url}长时间无响应")




def clean_iso(url):
    out = os.popen(f"git config --global --unset url.{url}.insteadof").read()
    if out:
        print("执行情况如下：\n", out)


def get_iso():
    out = os.popen(f"git config --global -l").read()
    url = re.findall(".*url\.(.*)\.insteadof.*", out)
    if url:
        url = url[0]
    else:
        url = "GitHub官方"
    return url


def ping_callback(args):
    url = args["下拉选择框"].get()
    ping_iso(url=url)


def clean_callback(args):
    clean_iso(get_iso())
    args["当前镜像源情况"].set(get_iso())
    print("清空完毕")


def set_callback(args):
    url = args["下拉选择框"].get()
    set_iso(url)
    args["当前镜像源情况"].set(get_iso())
    print("设置完毕")


def set_hosts(args):
    GitHubOptimizer()


def reset_hosts(args):
    GitHubOptimizer(RESET_FLAG)


class QWebSiteOptGUI:
    def __init__(self, title="QWebSiteOptimizer - GitHub"):
        # 基础GUI
        self.gui = CreateQGUI(title=title)
        self.gui.add_banner_tool(GitHub("https://github.com/QPT-Family/QWebSiteOptimizer"))
        self.gui.set_navigation_about(author="GT_ZhangAcer",
                                      version=__version__,
                                      github_url="https://github.com/QPT-Family/QWebSiteOptimizer")
        # DNS解析选优功能区
        set_dns_opt = BaseButton(bind_func=set_hosts, text="开始DNS选优", style="info")
        clear_dns_opt = BaseButton(bind_func=reset_hosts, text="清除DNS选优", style="success")
        self.gui.add_notebook_tool(HorizontalToolsCombine(tools=[set_dns_opt, clear_dns_opt],
                                                          title="[ROOT] DNS解析选优 - 需要管理员权限",
                                                          text="通过对多个DNS返回的结果进行筛选，匹配当前网络环境下最快的解析地址并设置Host文件，"
                                                               "从而达到加速目的。\n"
                                                               "该方式虽然不如VPN稳定可靠，但在短期内我们可通过该加速效果来达到优化GitHub浏览速度等问题。\n"
                                                               "建议在阅览GitHub出现卡顿时重新进行设置，若需要Clone大型项目，可切换至镜像源模式进行解决。"))

        # 镜像源模式功能区
        act = get_iso()
        if not act:
            act = "GitHub官方"
        iso_act = Label(name="当前镜像源情况", text=act, title="当前镜像源:")
        iso_comb = Combobox(name="下拉选择框", title="选择镜像源:", options=ISO_LIST)

        iso_ping = BaseButton(bind_func=ping_callback, text="Ping测试", style="info")
        iso_clear = BaseButton(bind_func=clean_callback, text="清除镜像源", style="success")
        iso_set = BaseButton(bind_func=set_callback, text="设置镜像源", style="danger")

        iso_btn = HorizontalToolsCombine(tools=[iso_comb, iso_ping, iso_clear, iso_set])

        self.gui.add_notebook_tool(HorizontalFrameCombine(tools=[iso_act, iso_btn],
                                                          title="镜像源模式",
                                                          text="通过对GitHub默认源进行替换，从而快速从镜像源中加载我们需要的数据，提升Clone的效率。\n"
                                                               "但由于镜像源并非官方源，强烈、非常强烈建议我们仅在需要Clone公开项目时开启该模式，"
                                                               "在Push以及私有项目的操作中保持关闭状态，避免出现异常情况！"))

    def run(self):
        self.gui.run()


if __name__ == '__main__':
    # _u = "https://hub.fastgit.org"
    # set_iso(_u)
    # _a = get_iso()
    # print(_a)
    # clean_iso(_a[0])
    # _b = get_iso()
    # print("b:", _b)
    _a = QWebSiteOptGUI()
    _a.run()
