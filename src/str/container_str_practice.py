"""
演示字符串作为数据容器的相关操作
"""
# index
my_str = "hello world"
print(my_str.index(" "))  # 结果：5
# 通过下标索引取值
value1 = my_str[1]
value2 = my_str[-10]
print(f"从字符串{my_str}取下标为1的元素值为：{value1}，下标为-10的元素值为：{value2}")

# index方法
value = my_str.index("world")
print(f"在字符串{my_str}中查找world，其起始下标是：{value}")

# 字符串替换replace
new_str = my_str.replace("hello", "Hi,")
print(f"将字符串：{my_str}，进行替换后得到：{new_str}")

# split方法
split_str = "hello python world"
split_list = split_str.split(" ")
print(f"将字符串{split_str}进行split切分，得到：{split_list}，类型是：{type(split_list)}")

# strip方法
my_str = "  hello world    "
new_my_str = my_str.strip()  # 不传入参数，取出首尾空格
print(f"字符串{my_str}被strip后，结果：{new_my_str}")   # 结果：hello world

my_str = "12hello world 21"
new_my_str = my_str.strip("12")  # 不传入参数，取出首尾空格
print(f"字符串{my_str}被strip('12')后，结果：{new_my_str}")  # 结果：hello world

# 统计字符串中某字符串的出现次数，count
my_str = "hello world, hi, world!"
count = my_str.count("world")
print(f"字符串{my_str}中world出现的次数：{count}")

# 统计字符串的长度
my_str = "hello world! "
num = len(my_str)
print(f"字符串{my_str}的长度为：{num}")

"""
给定一个字符串："hello world, he is world, she is world!"
1. 统计字符串内有多少个"he"字符串
2. 将字符串内的空格，全部替换为：“|”
3. 按照“|”进行字符串分隔，得到列表
"""
my_str = "hello world, he is world, she is world!"
count = my_str.count("he")
print(f"统计字符串：{my_str}内有多少个he：{count}")
re_str = my_str.replace(" ", "|")
print(f"字符串：{my_str}的空格替换为“|”后的结果：{re_str}")

split_str = re_str.split("|")
print(f"字符串：{re_str}按照“|”进行字符串分隔，得到列表：{split_str}")
