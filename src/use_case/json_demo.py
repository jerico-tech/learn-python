"""
演示JSON数据和Python字典的相互转换
"""
# 导入json模块
import json
# 准备符合json格式要求的python数据
data=[{"name":"老王","age":16}, {"name":"张三","age":20}]

# 通过json.dumps(data)方法把python数据转化为了json数据
data = json.dumps(data, ensure_ascii=False)
print(type(data))
print(data)
# 通过json.loads(data)方法把json数据转化为了python数据
data = json.loads(data)
print(type(data))