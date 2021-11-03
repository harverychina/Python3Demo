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
print(list((1, 2, 3)))
# 将列表转成元组
print(tuple([1, 2, 3]))

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

# 列表和元组存储方式的差异
l4 = [1, 2, 3]
print(l.__sizeof__())

tup3 = (1, 2, 3)
print(tup3.__sizeof__())

l5 = []
print(l5.__sizeof__())  # 空列表的存储空间为40字节
l5.append(1)
print(l5.__sizeof__()) # 列表为其分配了可以存储4个元素的空间（72 -40）/8 = 4
l5.append(2)
print(l5.__sizeof__())  # 由于之前分配了空间所以加入元素2，列表空间不变
l5.append(3)
print(l5.__sizeof__())
l5.append(4)
print(l5.__sizeof__())
l5.append(5)  # 加入元素5之后，列表的空间不足，所以又额外分配了可以存储4个元素的空间（104 - 72）/ 8 = 4
print(l5.__sizeof__())

"""
测试列表和元组初始化和索引操作速度
"""
#  python3 -m timeit 'x=(1,2,3,4,5,6)'
# 50000000 loops, best of 5: 8.5 nsec per loop
# python3 -m timeit 'x=[1,2,3,4,5,6]'
# 5000000 loops, best of 5: 40.4 nsec per loop
# python3 -m timeit 'x=[1,2,3,4,5,6]' 'y=x[3]'
# 5000000 loops, best of 5: 58.8 nsec per loop
# python3 -m timeit 'x=(1,2,3,4,5,6)' 'y=x[3]'
# 10000000 loops, best of 5: 24.4 nsec per loop

# 元组使用场景：存储数据和数量不变，比如你有一个函数，需要返回的是一个地点的经纬度，然后直接传给前端渲染。
# 列表使用场景：存储数据和数量是可变，比如社交平台上的一个日志功能，是统计一个用户在一周之内看了哪些用户的帖子

"""
empty_list = list()    # 5000000 loops, best of 5: 50.6 nsec per loop
# 以上创建空列表，是使用function call，创建stack，进行一系列参数检查操作，所需时间会比下面的方式要长
empty_list = []        # 20000000 loops, best of 5: 15.3 nsec per loop
"""