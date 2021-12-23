# -*- coding:utf8 -*-
# @Time：2021/12/23 9:35 AM
# @Author： Huang Jeff

import sys

a = []

print(sys.getrefcount(a))

b = a

print(sys.getrefcount(a))

c = b
d = b
e = c
f = e
g = d

print(sys.getrefcount(a))
