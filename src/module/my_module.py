"""
演示自定义模块
"""
__all__ = ['test_a']

def test(a, b):
    print(a+b)

def test_a():
    print("test A")

def test_b():
    print("test B")



if __name__ == '__main__':
    test(1, 2)
