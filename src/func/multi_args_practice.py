"""
演示函数的多种参数使用示例
"""
def user_info(name, age, gender):
    print(f"您的名字是：{name}，年龄是：{age}，性别是：{gender}")
# 位置参数
user_info("小明", 20, "男")

# 关键字传参
user_info(name="小明", age = 20, gender="男")
# 可以不按照固定顺序
user_info(age = 20, gender="男", name="小明")
# 可以和位置参数混用，位置参数必须在前，且匹配参数顺序
user_info("小明", age=20, gender="男")

def user_info(name, age, gender='男'):
    print(f"您的名字是{name}, 年龄是{age}，性别是{gender}")

user_info('Tome', 20)
user_info('Rose', 22, '女')

# 不定长参数 -- 位置传递
def user_info(*args):
    print(f"args的类型：{type(args)}，内容是：{args}")

user_info('TOM')  # ('TOM',)
user_info('TOM', 18)  # ('TOM', 18)

# 关键字传递
def user_info(**kwargs):
    print(f"kwargs的类型：{type(kwargs)}，内容是：{kwargs}")

user_info(name='TOM', age=18, id=110) # {'name': 'TOM', 'age': 18, 'id': 110}
