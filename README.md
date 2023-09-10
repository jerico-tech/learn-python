# python基础
### 编码
默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。

### 标识符
- 第一个字符必须是字母表中字母或下划线 _ 。
- 标识符的其他的部分由字母、数字和下划线组成。
- 标识符对大小写敏感。

在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的了。
### python保留字
保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
```python 
import keyword
print("hello world!")
print(keyword.kwlist)  # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```
### 注释
#### 单行注释
Python中单行注释以 # 开头，实例如下：
```python
# 第一个注释
print ("Hello, Python!") # 第二个注释
```
#### 多行注释
多行注释可以用多个 # 号，还有 ''' 和 """：
```python
# 第一个注释
# 第二个注释
 
'''
第三注释
第四注释
'''
 
"""
第五注释
第六注释
"""
print ("Hello, Python!")
```
### 行与缩进
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
```python
# 演示注释和缩进
if True:
    print('True')
else:
    print('False')
```
### 多行语句
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句，例如：
```python
total = item_one + \
        item_two + \
        item_three
```
在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \，例如：
```python
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
```

