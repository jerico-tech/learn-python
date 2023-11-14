# 定义列表并用变量接收它，内容是：[21, 25, 21, 23, 22, 20]
list = [21, 25, 21, 23, 22, 20]

# 追加一个数字31到列表尾部
list.append(31)
# 追加一个新列表[29, 33, 30]到列表尾部
list_new = [29, 33, 30]
list.extend(list_new)
# 取出第一个元素，（应该是21）
num1 = list[0]
print(f"从列表中取出的第一个元素应该是21，实际是：{num1}")
# 取出最后一个元素（应该是30）
num2 = list[-1]
print(f"从列表中取出的最后一个元素应该是30，实际是：{num2}")
# 查找元素31，在列表中的下标位置
index = list.index(31)
print(f"元素31在列表中的下标位置是：{index}")
print(f"最后列表中的内容是：{list}")

def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    # 循环控制变量通过下标索引来控制，默认0
    # 每一次循环将下标索引变量+1
    # 循环条件：下标索引变量 < 列表的元素数量
    my_list = ["hello", "hi", "world", "ChatGLM"]
    index = 0
    while index < len(my_list):
        # 通过index取出对应下标的元素
        element = my_list[index]
        print(f"列表的元素：{element}")
        index += 1

list_while_func()

def list_for_func():
    """
    使用for循环变量列表的演示函数
    :return: None
    """
    my_list = [1, 2, 3, 4, 5]
    for element in my_list:
        print(f"列表中的元素有：{element}")

list_for_func()