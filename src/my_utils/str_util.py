"""
字符串相关的工具模块
"""

def str_reverse(s):
    """
    功能时将字符串完成反转
    :param s: 将被反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]

def substr(s, x, y):
    """
    按照给定下标完成给定字符串的切片
    :param s: 将被切片的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下标
    :return: 切片完成后的字符串
    """
    return s[x:y]


if __name__ == '__main__':
    print(str_reverse("hello"))
    print(substr("hello world", 1, 2))