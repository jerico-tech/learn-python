"""
演示自定义模块
"""
# 导入自定义模块使用
# import my_module
# from my_module import test
#
# my_module.test(1, 2)
# test(3, 2)

# 导入不同模块的同名功能
from my_module import test
from my_module2 import test
test(1, 2)

from my_module import *
test_a()
test_b()


