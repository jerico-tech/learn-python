"""
演示for循环的基础语法
"""

name = "jerico"

for x in name:
    # 将name的内容、挨个取出赋予x临时变量
    # 就可以在循环体内对x进行处理
    print(x)

"""
数一数有几个a
"""

name = "itheima is a brand of itcast"
count = 0
for x in name:
    if x == 'a':
        count += 1
print(f"总共有{count}个a")

"""
range练习
"""
for x in range(10):
    print(x)

for x in range(5, 10):
    # 从5开始，到10结束（不包含10）的一个数字序列，数字间隔为1
    print(x)

for x in range(5, 10, 2):
    # 从5开始，到10结束（不包含10）的一个数字序列，数字间隔为2
    print(x)

for i in range(5):
    print(i)
print(i)