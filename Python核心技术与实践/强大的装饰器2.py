# -*- coding:utf8 -*-
# @Time：2021/12/7 9:23 AM
# @Author： Huang Jeff

# 参数变化时, *args和**kwargs，表示接受任意数量和类型的参数
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)
    return wrapper


@my_decorator
def greet(message, name):
    print(message, name)


greet('hello world', 'tom')


# 带有自定义参数的装饰器，记录函数执行的次数
def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)
        return wrapper
    return my_decorator


@repeat(4)
def greet(message):
    print(message)


greet('hello world')
print('------------')
print(greet.__name__)
# 打印出元信息，显示它不是以前的那个greet()函数，而被wrapper()函数取代了
help(greet)
