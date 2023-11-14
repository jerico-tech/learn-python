# 查询元素的下标
mylist = ["tom", "lily", "lucy"]
index = mylist.index("lily")
print(index)

mylist[0] = "张三"
mylist.insert(1, "李四")
mylist.append("append最后一个元素")
mylist2 = [1,2,3]
mylist.extend(mylist2)
print(mylist)

del mylist2[2]
element = mylist2.pop(0)
print(f"{mylist2} , {element}")

lists = ["test","java","test","python"]
print(f"len= {len(lists)}")
count = lists.count("test")
print(count)
lists.remove("test")
lists.clear()
print(lists)