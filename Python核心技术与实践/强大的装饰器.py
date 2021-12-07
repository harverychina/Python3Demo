# -*- coding:utf8 -*-
# @Time：2021/12/7 8:47 AM
# @Author： Huang Jeff

def func(message):
    print('Got a message: {}'.format(message))


# 把函数func赋予了变量send_message，这样之后你调用send_message，就相当于是调用函数func()
send_message = func
send_message('hello world')


def get_message(message):
    return 'Got a message: ' + message


# 把函数get_message以形参数的形式，传入了函数root_call()中然后调用它
def root_call(func, message):
    print(func(message))


root_call(get_message, 'hello world')


# 可以在函数里定义函数，也就是函数的嵌套
def func(message):
    def get_message(message):
        print('Got a message: {}'.format(message))
    return get_message(message)


func('hello world')


"""
闭包,函数 func_closure() 的返回值是函数对象 get_message 本身，之后，我们将其赋予变量 send_message，再调用 send_message(‘hello world’)，最后输出了'Got a message: hello world'。
"""


def func_closure():
    def get_message(message):
        print('Got a message: {}'.format(message))
    return get_message


send_message = func_closure()
send_message('hello world')


# 装饰器
"""
变量 greet 指向了内部函数 wrapper()，而内部函数 wrapper() 中又会调用原函数 greet()，因此，最后调用 greet() 时，就会先打印'wrapper of decorator'，然后输出'hello world'。
"""


def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper


# 这里的函数 my_decorator() 就是一个装饰器，它把真正需要执行的函数 greet() 包裹在其中，并且改变了它的行为，但是原函数
# greet() 不变。

def greet():
    print('hello world')


greet = my_decorator(greet)
greet()


# 语法糖，更简单、更优雅

def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper


@my_decorator  # 等同于: greet = my_decorator(greet)
def greet():
    print('hello world')


greet()


# 带参数的装饰器

def my_decorator(func):
    def wrapper(message):
        print('wrapper of decorator')
        func(message)
    return wrapper


@my_decorator
def greet(message):
    print(message)


greet('hello world')


