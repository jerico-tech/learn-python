"""
演示异常、模块、包的综合案例练习
"""
# 创建my_utils包，在包内创建：str_util.py和file_util.py 2个模块，并提供相应的函数

import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("world"))
print(my_utils.str_util.substr("world", 0,2))

file_util.print_file_info("D:/append.txt")
file_util.append_to_file("D:/append.txt", "main")
file_util.print_file_info("D:/append.txt")