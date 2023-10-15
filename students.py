"""
演示面向对象类中成员方法的定义和使用
"""

# 定义一个方法
class Student:
    """
        如果定义了构造方法，且在构造方法内部对变量进行赋值，此处定义可以省略。
        构造方法内部相当于完成变量声明和赋值
    """
    name = None  # 学生姓名
    age = None  # 学生年龄

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f"大家好，我是{self.name}，请大家多多关照")

    def say_hi2(self, msg):
        print(f"大家好，我是：{self.name}，{msg}")

    # 定义__str__魔术方法
    def __str__(self):
        return f"Student类对象，name:{self.name},age:{self.age}"

    # 定义__lt__魔术方法
    def __lt__(self, other):
        return self.age < other.age

    # 定义__le__魔术方法
    def __le__(self, other):
        return self.age <= other.age

    # 定义__eq__魔术方法
    def __eq__(self, other):
        return self.age == other.age

stu = Student("周杰伦", 31)
stu.say_hi()
stu.say_hi2("哎呀，不错呀")

stu2 = Student("林俊杰", 36)
stu2.say_hi()
stu2.say_hi2("nice to meet you!")

print(stu < stu2)   # True
print(stu > stu2)   # False
print(stu <= stu2)   # True
print(stu >= stu2)   # False
stu3 = Student("林俊杰", 36)
stu4 = Student("林俊杰", 36)
print(stu3 == stu4)   # True
