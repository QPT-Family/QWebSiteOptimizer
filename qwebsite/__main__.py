# Author: Acer Zhang
# Datetime: 2021/9/8 
# Copyright belongs to the author.
# Please indicate the source for reprinting.

import click
from qwebsite.base import GitHubOptimizer
from qwebsite.flags import *


@click.command()
@click.option("-r",
              "--reset",
              type=bool,
              default=False,
              help="恢复模式")
def cli(reset):
    if reset:
        GitHubOptimizer(mode=RESET_FLAG)
    else:
        GitHubOptimizer()


if __name__ == '__main__':
    cli()
