"""
演示Python的模块导入
"""
# # 使用import导入time模块使用sleep功能（函数）
# import time   # 导入Python内置的time模块（time.py这个代码文件）
# print("你好")
# time.sleep(5)
# print("我好")
#
# # 使用from导入time的sleep功能（函数）
# from time import sleep
# print("开始")
# sleep(1)
# print("结束")

# 使用*导入time模块的全部功能
from time import *
print("hello")
sleep(5)
print("bye")

# 使用as给特定功能加上别名
import time as t
print("hello")
sleep(2)
print("bye")

from time import sleep as sl
print("hello")
sl(2)
print("bye")
