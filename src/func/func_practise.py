"""
演示函数使用参数
"""
# 定义2数相加的函数，通过参数接收两个参数
def add(x, y):
    """
    add 函数可以接收两个参数，进行2相加的功能
    :param x: 形参表示相加的一个数字
    :param y: 形参表示相加的另一个数字
    :return: 返回是2数相加的结果
    """
    result = x + y
    print(f"{x}+{y}={result}")
    return result

# 函数调用
r = add(1, 2)
print(f"计算结果：{r}")
"""
自动查核酸
"""
# 定义函数：接收一个形式参数，数字类型，表示体温
def check(temprature):
    # 函数体内进行判断体温
    print(f"欢迎来到黑马程序员，请出示您的健康码以及72小时核酸证明，并配合测量体温！")
    if temprature > 37.5:
        print(f"可不进入")
    else:
        print(f"可以进入")

# 调用函数，传入实际参数
check(37.8)

# 主动返回None的函数
def say_hi():
    print("你好呀")
    return None

# None用于if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None

result = check_age(16)
if not result:
    # 进入if表示result是None值，也就是False
    print("未成年，不可以进入")

# global关键字
num = 100

def testA():
    print(num)

def testB():
    # global关键字声明num是全局变量
    global num
    num = 200
    print(num)

testA()  # 100
testB()  #200
print(num) # 200,，使用global把num改为200，如果不加global结果则是100