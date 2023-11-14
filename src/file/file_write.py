"""
演示文件的写入
"""
# 1.打开文件
f = open("D:/test.txt", "w", encoding="UTF-8")

# 2.文件写入：write写入
f.write("hello world!")

# 3.内容刷新：flush()
f.flush()

# 4.关闭文件 close
f.close()


# 打开不存在的文件
f = open("D:/append.txt", "a")
# write写入
f.write("hello world!")
# flush()
f.flush()
# close关闭
f.close()