# coding:utf8
# 读取文件，将内容转化成为列表list数据结构显示
lst = [line.strip() for line in open('data.txt')]
print(lst)
# 以上语句可以用下面传统的方式展开理解
list(open("data.txt"))
with open("data.txt") as f:
    lst = [line.strip() for line in f]
print(lst)
