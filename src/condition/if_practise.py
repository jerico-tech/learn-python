age = 10

if age >= 18:
    print("我已经成年了")
    print("即将步入大学生活")
print("时间过的真快啊")

# 练习题
print("欢迎来到动物园参观，儿童免费，成人收费。")
age = input("请输入你的年龄：")

if int(age) >= 18:
    print("您已成年，游玩需要补票10元。")
else:
    print("您未成年，可以免费游玩。")
print("祝您游玩愉快！")

# 练习：我要买票吗
height = int(input("请输入你的身高："))
if height > 120:
    print("你的身高超出120cm，需要买票：10元。")
else:
    print("您的身高低于120cm，可以免费游玩。")

# if elif else多条件判断语句的使用
height = int(input("请输入你的身高（cm）："))
vip_level = int(input("请输入你的VIP等级（1-5）："))

if height < 120:
    print("身高小于120cm，可以免费。")
elif vip_level > 3:
    print("vip级别大于3，可以免费。")
else:
    print("不好意思，条件都不满足，需要买票10元。")