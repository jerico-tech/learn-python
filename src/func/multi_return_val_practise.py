"""
演示函数的多返回值
"""

def test_return():
    return 1,"hello", True
x, y, z = test_return()
print(x)  # 结果1
print(y)  # 结果"hello"
print(z)  # 结果True
