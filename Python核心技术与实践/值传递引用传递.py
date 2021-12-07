# -*- coding:utf8 -*-
# @Time：2021/12/7 8:41 AM
# @Author： Huang Jeff

def func(d):
    d['a'] = 10
    d['b'] = 20


d = {'a': 1, 'b': 2}
print(func(d))
print(d)
