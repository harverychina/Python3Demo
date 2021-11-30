# -*- coding:utf8 -*-
# @Time：2021/11/30 9:25 上午
# @Author： Huang Jeff
"""
对于整数， a is b 为 True的结论，只适用于-5 到 256范围的数字
"""

import copy
a = 257
b = 257

print(a == b)

print(id(a))

print(id(b))

print(a is b)  # True
# 在交互方式中，输出 False

# 对于元组，使用tuple()或者切片操作":"不会创建一份浅浅贝，相反，它会返回一个指向相同元组的引用
t1 = (1, 2, 3)
t2 = tuple(t1)
print(t1 == t2)
print(t1 is t2)

# 浅拷贝
l1 = [[1, 2], (30, 40)]
l2 = list(l1)
l1.append(100)
l1[0].append(3)
print(l1)
print(l2)

l1[1] += (50, 60)
print(l1)
print(l2)

"""
比较操作符'=='表示比较对象间的值是否相等，而'is'表示比较对象的标识是否相等，即它们是否指向同一个内存地址。
比较操作符'is'效率优于'=='，因为'is'操作符无法被重载，执行'is'操作只是简单的获取对象的 ID，并进行比较；而'=='操作符则会递归地遍历对象的所有
值，并逐一比较。
浅拷贝中的元素，是原对象中子对象的引用，因此，如果原对象中的元素是可变的，改变其也会影响拷贝后的对象，存在一定的副作用。
深度拷贝则会递归地拷贝原对象中的每一个子对象，因此拷贝后的对象和原对象互不相关。另外，深度拷贝中会维护一个字典，记录已经拷贝的对象及其 ID，
来提高效率并防止无限递归的发生。
"""

# 思考题
x = [1]
y = x.append(x)

y = copy.deepcopy(x)

# print(x == y)
# 程序会报错：'RecursionError: maximum recursion depth exceeded in
# comparison'。因为x是一个无限嵌套的列表，y深度拷贝x也是一个无限嵌套的列表，理论上x==y应该返回True，但是x==y内部执行是会递归遍历列表x和y中每一个元素的值，由于x和y是无限嵌套的，因此会stack
# overflow，报错
