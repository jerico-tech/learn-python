"""
演示对序列进行切片操作
"""

# 对list进行切片，从1开始，4结束，步长1
my_list = [0, 1, 2, 3, 4, 5, 6]
result1 = my_list[1:4]  # 步长默认是1，所以可以省略不写
print(f"结果1：{result1}")

# 对tuple进行切片，从头开始，到最后结束，步长1
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[:]  # 起始和结束位置不写表示从头到尾，步长为1可以省略
print(f"结果2：{result2}")

# 对str进行切片，从头开始，到最后结束，步长2
my_str = "01234567"
result3 = my_str[::2]  # 起始和结束位置不写表示从头到尾，步长为1可以省略
print(f"结果3：{result3}")

# 对str进行切片，从头开始，到最后结束，步长-1
result4 = my_str[::-1]
print(f"结果4：{result4}")  # 等同于序列反转了
# 对列表进行切片，从3开始，到1结束，步长-1
result5 = my_str[3:1:-1]
print(f"结果5：{result5}")
# 对元组进行切片，从头开始，到结尾结束，步长-2
result6 = my_str[::-2]
print(f"结果6：{result6}")

"""
有字符串：“万过薪月，员序程马黑来，nohtyP学”
请使用学过的任何方式，得到黑马程序员
"""
# 方式一
my_str = "万过薪月，员序程马黑来，nohtyP学"
split_str = my_str.split("，")
print(f"结果：{split_str[1][4::-1]}")

# 方式二
result = my_str[5:10][::-1]
print(f"结果：{result}")

# 方式三
result = my_str[9:4:-1]
print(f"结果：{result}")