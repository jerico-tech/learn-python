"""
演示函数作为参数的示例
"""
def test_func(computer):
    result = computer(1, 2)
    print(result)

def computer(x, y):
    return x + y

test_func(computer)

# lambda匿名函数
def test_func(computer):
    result = computer(1, 2)
    print(result)

test_func(lambda x,y:x * y)