# Author: Acer Zhang
# Datetime: 2021/9/8 
# Copyright belongs to the author.
# Please indicate the source for reprinting.

from setuptools import setup
from setuptools import find_packages
from qwebsite import __version__

# python setup.py sdist bdist_wheel
setup(
    name='QWebSite',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/QPT-Family/QWebSiteOptimizer',
    license='LGPL',
    author='GT-ZhangAcer',
    author_email='zhangacer@foxmail.com',
    description='QWebSite',
    install_requires=["click",
                      "ping3"],
    python_requires='>3.5',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'qwebsite = qwebsite.__main__:cli',
        ]}
)
