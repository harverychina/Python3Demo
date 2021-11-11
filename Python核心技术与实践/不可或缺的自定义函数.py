# -*- coding:utf8 -*-
# @Time：2021/11/11 10:23 上午
# @Author： Huang Jeff
"""
第一，函数的嵌套能够保证内部函数的隐私。内部函数只能被外部函数所调用和访问，不会暴露在全局作用域，
因此，如果你的函数内部有一些隐私数据（比如数据库的用户、密码等），不想暴露在外，
那你就可以使用函数的的嵌套，将其封装在内部函数中，只通过外部函数来访问。
"""

# def connect_DB():
#     def get_DB_configuration():
#         ...
#         return host, username, password
#     conn = connector.connect(get_DB_configuration())
#     return conn

# 第二，合理的使用函数嵌套，能够提高程序的运行效率。

# def factorial(input): # validation check
#     if not isinstance(input, int):
#         raise Exception('input must be an integer.')
#     if input < 0:
#         raise Exception('input must be greater or equal to 0' )
#     ...
#
# def inner_factorial(input):
#     if input <= 1:
#         return 1
#     return input * inner_factorial(input-1)
# return inner_factorial(input)
#
# print(factorial(5))

# 在全局变量要在函数当中使用，需要加global关键字
# MIN_VALUE = 1MAX_VALUE = 10
# def validation_check(value):
#     global MIN_VALUE
#     ...
#     MIN_VALUE += 1
#     ...
# validation_check(5)

# 局部变量和全局变量同名时，则按内部变量来处理，同时内部变量是无法改变外部变量的值
# 若要修改，则要加nonlocal关键字


def outer():
    x = "local"

    def inner():
        nonlocal x  # nonlocal关键字表示这里的x就是外部函数outer定义的变量x
        x = 'nonlocal'
        print("inner:", x)
    inner()
    print("outer:", x)


outer()
# 输出
# inner: nonlocal
# # outer: nonlocal

# 闭包


def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of


square = nth_power(2)
cube = nth_power(3)
print(type(square))
print(type(cube))
print(square)
print(cube)
print(square(2))
print(cube(2))
