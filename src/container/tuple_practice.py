# 定义元组
t1 = (1, "hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是:{type(t1)}，内容是：{t1}")
print(f"t2的类型是:{type(t2)}，内容是：{t2}")
print(f"t3的类型是:{type(t3)}，内容是：{t3}")

# 定义单个元素的元组
t4 = ("hello",)
print(f"t4的类型是:{type(t4)}，内容是：{t4}")

# 元组的嵌套
t5 = ((1,2,3),(4,5,6))
print(f"t5的类型是:{type(t5)}，内容是：{t5}")

# 下标索引去取出内容
element = t5[1][-1]
print(f"从嵌套元组中取出的数据是：{element}")

# 元组的操作：index查找方法
t6 = ("java", "python", "javascript", "C", "C++")
index = t6.index("python")
print(f"在元组t6中查找python，下标是：{index}")

# 元组的操作：count统计方法
t7 = ("java", "python", "javascript", "C", "C++", "Python")
num = t7.count("python")
print(f"在元组t7中统计python的数量：{num}个")
# 元组的操作：len函数统计元组的数量
t8 = ("java", "python", "javascript", "C", "C++", "Python")
num = len(t8)
print(f"在元组t8中元素的个数：{num}个")

# 元组的遍历：while
index = 0
while index < len(t8):
    print(f"【while】元组的元素有：{t8[index]}")
    # 至关重要
    index += 1

# 元组的遍历：for
for ele in t8:
    print(f"【for】元组的元素有：{ele}")

# 修改元组中的列表的值
t9 = (1,2, ["python", "php"],)
print(f"t9元组中的内容“{t9}")   # t9元组中的内容“(1, 2, ['python', 'php'])
t9[2][1] = "java"
t9[2].append("C")
print(f"t9元组中的内容“{t9}")   # t9元组中的内容“(1, 2, ['python', 'java'])