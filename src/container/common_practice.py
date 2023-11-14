"""
演示数据容器的通用功能
"""
my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = "abcdefg"
my_set = {1,2,3,4,5}
my_dict = {"key1":1, "key2":2, "key3":3, "key4":4, "key5":5}

# len元素个数
print(f"列表 元素个数：{len(my_list)}")
print(f"元组 元素个数：{len(my_tuple)}")
print(f"字符串 元素个数：{len(my_str)}")
print(f"集合 元素个数：{len(my_set)}")
print(f"字典 元素个数：{len(my_dict)}")

# max最大元素
print(f"列表 最大的元素：{max(my_list)}")
print(f"元组 最大的元素：{max(my_tuple)}")
print(f"字符串 最大的元素：{max(my_str)}")
print(f"集合 最大的元素：{max(my_set)}")
print(f"字典 最大的元素：{max(my_dict)}")

# min最小元素
print(f"列表 最小的元素：{min(my_list)}")
print(f"元组 最小的元素：{min(my_tuple)}")
print(f"字符串 最小的元素：{min(my_str)}")
print(f"集合 最小的元素：{min(my_set)}")
print(f"字典 最小的元素：{min (my_dict)}")

# 类型转换：容器转列表
print(f"列表 转 列表 的结果是：{list(my_list)}")
print(f"元组 转 列表 的结果是：{list(my_tuple)}")
print(f"字符串 转 列表 的结果是：{list(my_str)}")
print(f"集合 转 列表 的结果是：{list(my_set)}")
print(f"字典 转 列表 的结果是：{list(my_dict)}")

# 类型转换：容器转元组
print(f"列表 转 元组 的结果是：{tuple(my_list)}")
print(f"元组 转 元组 的结果是：{tuple(my_tuple)}")
print(f"字符串 转 元组 的结果是：{tuple(my_str)}")
print(f"集合 转 元组 的结果是：{tuple(my_set)}")
print(f"字典 转 元组 的结果是：{tuple(my_dict)}")

# 类型转换：容器转字符串
print(f"列表 转 字符串 的结果是：{str(my_list)}")   # "[1, 2, 3, 4, 5]"
print(f"元组 转 字符串 的结果是：{str(my_tuple)}")  # "(1, 2, 3, 4, 5)"
print(f"字符串 转 字符串 的结果是：{str(my_str)}")  # "abcdefg"
print(f"集合 转 字符串 的结果是：{str(my_set)}")    # "{1, 2, 3, 4, 5}"
print(f"字典 转 字符串 的结果是：{str(my_dict)}")   # "{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}"

# 类型转换：容器转集合
print(f"列表 转 集合 的结果是：{set(my_list)}")
print(f"元组 转 集合 的结果是：{set(my_tuple)}")
print(f"字符串 转 集合 的结果是：{set(my_str)}")
print(f"集合 转 集合 的结果是：{set(my_set)}")
print(f"字典 转 集合 的结果是：{set(my_dict)}")

# 容器的排序
my_list = [3, 1,2,3, 5, 4]
my_tuple = (3, 1,2,3, 5, 4)
my_str = "bdcefga"
my_set = {3, 1,2,3, 5, 4}
my_dict = {"key3":1, "key1":2, "key2":3, "key4":4, "key5":5}

print(f"列表 排序后的结果：{sorted(my_list)}， 原始的列表内容：{my_list}")
print(f"元组 排序后的结果：{sorted(my_tuple)}， 原始的元组内容：{my_tuple}")
print(f"字符串 排序后的结果：{sorted(my_str)}")
print(f"集合 排序后的结果：{sorted(my_set)}")
print(f"字典 排序后的结果：{sorted(my_dict)}")

print(f"列表 反向排序后的结果：{sorted(my_list, reverse=True)}")
print(f"元组 反向排序后的结果：{sorted(my_tuple , reverse=True)}")
print(f"字符串 反向排序后的结果：{sorted(my_str, reverse=True)}")
print(f"集合 反向排序后的结果：{sorted(my_set, reverse=True)}")
print(f"字典 反向排序后的结果：{sorted(my_dict, reverse=True)}")