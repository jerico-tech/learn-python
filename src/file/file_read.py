"""
演示对文件的读取
"""
# 打开文件
f = open("D:\\02-work\\01-developer\\test.txt", 'r', encoding="UTF-8")
print(type(f))

# 读取文件 - read()
print(f"读取3个字节的结果：{f.read(3)}")
print(f"读取方法多钱全部内容的结果：{f.read()}")
print("----------------------------------")

# 读取文件 - readlines()
lines = f.readlines()  # 读取文件的全部行，封装到列表中
print(f"lines对象的类型：{type(lines)}")
print(f"lines对象的内容：{lines}")

# 读取文件 - readline()
line1= f.readline()
line2= f.readline()
line3= f.readline()
line4= f.readline()
print(f"第一行数据是：{line1}")
print(f"第二行数据是：{line2}")
print(f"第三行数据是：{line3}")
print(f"第四行数据是：{line4}")

# for循环读取文件行
for line in f:
    print(f"每一行数据：{line}")

# 关闭文件
f.close()

# with open
with open("D:\\02-work\\01-developer\\test.txt", 'r', encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line}")

