"""
演示数据容器字典的定义
"""

# 定义字典
my_dict = {"王力宏": 99, "周杰伦":88, "林俊杰":77 }

# 定义空字典
my_empty_dict1 = {}
my_empty_dict2 = dict()

print(f"my_dict的内容是：{my_dict}，类型是：{type(my_dict)}")
print(f"my_empty_dict1的内容是：{my_empty_dict1}，类型是：{type(my_empty_dict1)}")
print(f"my_empty_dict2的内容是：{my_empty_dict2}，类型是：{type(my_empty_dict2)}")

# 定义重复key的字典
my_dup_dict = {"王力宏": 99, "王力宏":88, "林俊杰":77 }
print(f"重复key的字典内容是：{my_dup_dict}")

my_dict = {"王力宏": 99, "周杰伦":88, "林俊杰":77 }
sorce = my_dict["王力宏"]
print(f"王力宏的考试分数是：{sorce}")  # 王力宏的考试分数是：99

# 定义嵌套字典
stu_score_dict = {
    "王力宏":{
        "语文":77,
        "数学":66,
        "英语":33
    },"周杰伦":{
        "语文":88,
        "数学":86,
        "英语":55
    },"林俊杰":{
        "语文":99,
        "数学":96,
        "英语":66
    }
}
print(f"学生的考试信息是：{stu_score_dict}")

# 从嵌套字典中获取数据：我想看周杰伦的语文成绩
score = stu_score_dict["周杰伦"]["语文"]
print(f"周杰伦的语文分数是：{score}")
score = stu_score_dict["林俊杰"]["英语"]
print(f"林俊杰的英语分数是：{score}")

"""
演示字典的常用操作
"""
my_dict = {"王力宏": 99, "周杰伦":88, "林俊杰":77 }

# 新增元素
my_dict["张三"] = 65
print(f"字典经过新增元素后，结果：{my_dict}")
# 更新元素
my_dict["周杰伦"] = 70
print(f"字典经过更新元素后，结果：{my_dict}")

# 删除元素
ele = my_dict.pop("周杰伦")
print(f"字典被移除一个元素后的字典：{my_dict}， 周杰伦的考试分数是：{ele}")
# 清空字典
my_dict.clear()
print(f"字典被清空后的字典：{my_dict}")

# 获取字典中的全部key
keys = stu_score_dict.keys()
print(f"字典的全部keys是：{keys}")

# 遍历字典
# 方式一：通过获取全部key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{stu_score_dict[key]}")

# 方式二：直接对字典进行for循环，每一次循环都是直接得到key
for key in stu_score_dict:
    print(f"2字典的key是：{key}")
    print(f"2字典的value是：{stu_score_dict[key]}")

# 统计字典的元素数量
num = len(stu_score_dict)
print(f"字典中元素的数量：{num}")