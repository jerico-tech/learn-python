"""
演示捕获异常
"""
# 基本捕获方法
try:
    f = open("D:/linux.txt", "r")
except:
    print("出现异常了，因为文件不存在，我将open的模式改为w模式打开")
    f = open("linux.txt", "w")

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print("name变量名未定义错误")

# 捕获多个异常
try:
    1/0
    print(name)
except (NameError, ZeroDivisionError) as e:
    print("出现了变量未定义 或 除以0的异常错误")

# 捕获所有异常
try:
    f = open("D:/123.txt", "r")
except Exception as e:
    print("出现异常了")
    print(e)

# else和异常的finally
try:
    print(1)
except Exception as e:
    print(e)
else:
    print("我是else，是没有异常的时候执行的代码")
finally:
    print("我是finally，有没有异常我都要执行")


