"""
演示数据容器集合的使用
"""
# 定义集合
my_set = {"java", "python", "C", "C++", "java", "LangChain"}
my_empty_set = set()
print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")  # {'python', 'java', 'C++', 'LangChain', 'C'}，类型是：<class 'set'>
print(f"my_empty_set的内容是：{my_empty_set}，类型是：{type(my_empty_set)}")

# 添加新元素
my_set = {"hello", "world"}
my_set.add("python")
my_set.add("hello")
print(f"my_set添加新元素后结果是：{my_set}") # {'world', 'hello', 'python'}

# 移除元素
my_set = {"hello", "world"}
my_set.remove("hello")
print(f"my_set移除hello后结果是：{my_set}") # {'world'}

# 从集合中随机取出元素
my_set = {"hello", "world"}
ele = my_set.pop()
print(f"my_set被取出元素：{ele} ，取出元素后结果是：{my_set}")

# 清空集合
my_set.clear()
print(f"集合被清空啦，结果是：{my_set}")

# 取出两个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(f"取出差集后的结果是：{set3}")
print(f"取出差集后，原有set1的内容是：{set1}")
print(f"取出差集后，原有set2的内容是：{set2}")

# 消除2个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference_update(set2)
print(f"消除差集后的结果是：{set3}")  # None
print(f"消除差集后，原有set1的内容是：{set1}")
print(f"消除差集后，原有set2的内容是：{set2}")

# 两个集合合并
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(f"两集合合并后的结果是：{set3}")
print(f"两集合合并后，set1的内容是：{set1}")
print(f"两集合合并后，set2的内容是：{set2}")

# 统计集合元素的数量len()
set1 = {1,2,3,4,5,1,2,3,4,5}
num = len(set1)
print(f"集合内的元素数量有：{num}个")  # 5个

# 集合的遍历
# 集合不支持下标索引，不能用while循环
# 可以用for循环
set1 = {1,2,3,4,5,1,2,3,4,5}
for ele in set1:
    print(f"集合的元素有:{ele}")

"""
有如下列表对象，对列表进行去重：
my_list = ['java','python', 'C', 'C++','java', 'C']
"""
my_list = ['java','python', 'C', 'C++','java', 'C']
my_set = set()
for ele in my_list:
    my_set.add(ele)

print(f"列表的内容：{my_list}，\n通过for循环后，得到集合的结果：{my_set}")
