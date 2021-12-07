# -*- coding:utf8 -*-
# @Time：2021/12/7 10:23 AM
# @Author： Huang Jeff

# 装饰器嵌套

import functools


def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator1')
        func(*args, **kwargs)
    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator2')
        func(*args, **kwargs)
    return wrapper


# 嵌套也是按先后顺序进行执行
@my_decorator1
@my_decorator2
def greet(message):
    print(message)


greet('hello world')
