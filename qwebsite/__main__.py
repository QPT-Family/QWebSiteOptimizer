# Author: Acer Zhang
# Datetime: 2021/9/8 
# Copyright belongs to the author.
# Please indicate the source for reprinting.

import click
from qwebsite.base import GitHubOptimizer
from qwebsite.flags import *
from qwebsite.submethod.github import QWebSiteOptGUI


@click.command()
@click.option("-g",
              "--gui",
              type=bool,
              default=True,
              help="图形化界面模式")
@click.option("-r",
              "--reset",
              type=bool,
              default=False,
              help="恢复模式")
def cli(gui, reset):
    if gui:
        QWebSiteOptGUI().run()
    else:
        if reset:
            GitHubOptimizer(mode=RESET_FLAG)
        else:
            GitHubOptimizer()


if __name__ == '__main__':
    cli([])
