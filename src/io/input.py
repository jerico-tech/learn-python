print("请告诉我你是谁？")
name = input()
print("我知道了，你是：%s" % name)

name = input("请告诉我你是谁？")
print("我知道了，你是：%s" % name)

# 输入数字类型
num = input("请告诉你的银行卡密码：")
num = int(num)
print("你的银行卡密码的类型是：", type(num))

# 欢迎登录小程序练习
user_name = input()
user_type = input()
print("您好：%s，您是尊贵的：%s用户，欢迎您的光临" % (user_name, user_type))