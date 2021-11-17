# -*- coding:utf8 -*-
# @Time：2021/11/16 10:56 上午
# @Author： Huang Jeff
"""
以lambda名字命名的函数，即是匿名函数
"""
# 2的3次方
# square = lambda x: x ** 2
# print(square(3))
# 让程序简洁
import operator
from functools import reduce
squares = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(list(squares))

# 循环0到10数字的平方
print([(lambda x: x * x)(x) for x in range(10)])

l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort(key=lambda x: x[1])  # 按列表第二个元素从小到大排序
print(l)

# map函数
l = [1, 2, 3, 4, 5]
new_list = list(map(lambda x: x * 2, l))
print(new_list)

# 函数式编程，将列表元素加倍


def mutiply_2_pure(l):
    new_list = []
    for item in l:
        new_list.append(item * 2)
    return new_list


print(mutiply_2_pure([1, 2, 3, 4]))

# filter函数
l = [1, 2, 3, 4, 5, 6, 8]
new_list = list(map(lambda x: x % 2 == 0, l))
print(new_list)

# rendce函数 计算阶乘
product = reduce(lambda x, y: x * y, l)
print(product)

# 思考题 将字典按值从大到小排序
d = {"mike": 10, "lucy": 2, "ben": 30}
print(d.items())
sort_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
print(sort_d)
