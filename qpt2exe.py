# Author: Acer Zhang
# Datetime:2021/9/29 
# Copyright belongs to the author.
# Please indicate the source for reprinting.

from qpt.executor import CreateExecutableModule

cem = CreateExecutableModule(work_dir="./qwebsite",
                             launcher_py_path="./qwebsite/run.py",
                             save_path="M:/QwebSite_Build",
                             requirements_file="./qwebsite/requirements_with_opt.txt")
cem.make()