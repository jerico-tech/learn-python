"""
演示while循环的基础应用
"""
i= 0
while i < 100:
    print("小美，你好！")
    i+= 1

"""
while求1-100的和
"""
j = 1
sum = 0
while j <= 100:
    sum += j
    j += 1
print(f"1-100的和：{sum}")
print("1-100的和：%d" % sum)


if False:
    """
    演示while循环的基础案例 - 猜数字
    """
    import random
    num = random.randint(1, 100)

    while True:
        user_num = int(input("请输入你猜的数字："))
        if user_num > num:
            print("你猜大了")
        elif user_num < num:
            print("你猜小了")
        else:
            print("恭喜你，猜中了！")
            break



"""
演示while循环的嵌套使用
"""
# 外层：表白100天的控制
# 内层： 每天的表白都送10只玫瑰花的控制

i = 1
while i <= 100:
    print(f"今天是第{i}天 ")

    # 内层循环控制变量
    j = 1
    while j <= 10:
        print(f"送给小美第{j}只玫瑰花")
        j += 1

    print("小美，我喜欢你")

    i += 1

print(f"坚持到第{i-1}天，表白成功")