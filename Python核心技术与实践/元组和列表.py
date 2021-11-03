# -*- coding:utf8 -*-
# @Time：2021/11/2 10:36 上午
# @Author： Huang Jeff

"""
都是一个可以放置任意数据类型的有序数据
列表是动态：长度大小不固定，可以随意地增加、删除或得改变元素
而元组是静态，长度大小不固定，无法增加删减或者改变
"""

l = [1, 2, 3, 4]
l[3] = 40
# print(l)
l.append(5)
print(l)

tup = (1, 2, 3, 4)
print(tup)
# tup[3] = 40
# TypeError: 'tuple' object does not support item assignment

# 那么元组就没有办法增加新元素了吗？不，可以，只是创建一个新的元组将旧元组和新元素依次填充进来
new_tup = tup + (5,)
# print(new_tup)

# 列表和元组都支持负数索引
print(l[-1])
print(tup[-1])

# 列表和元组支持切片操作
print(l[1:3])     # 返回列表中索引从1到2的子列表
print(tup[1:3])   # 返回元组中索引从1到2的子元组

# 列表和元组都可以随意嵌套
l2 = [[1, 2, 3], [4, 5]]
tup2 = ((1, 2, 3), (4, 5, 6))
# 将元组转成列表
print(list((1, 2 ,3)))
# 将列表转成元组
print(tuple([1 , 2 , 3]))

"""
列表和元组常用的内置函数
count()     统计元素出现次数
index()     元素的位置（索引）
reverse()   反序
sort()      排序
"""
l3 = [3, 2, 3, 7, 8, 1]
print(l3.count(3))
print(l3.index(7))
l3.reverse()
print(l3)
l3.sort()
print(l3)

