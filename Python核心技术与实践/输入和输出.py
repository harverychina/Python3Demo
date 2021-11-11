# -*- coding:utf8 -*-
# @Time：2021/11/10 8:41 上午
# @Author： Huang Jeff

# name = input('your name:')
# gender = input('you are a boy?(y/n)')


# welcome_str = 'Welcome to the matrix {prefix} {name}.'

# welcome_dic = {
#     'prefix': 'Mr.' if gender == 'y' else 'Mrs.',
#     'name': name
# }
#
# print('authorizing...')
# print(welcome_str.format(**welcome_dic))
# input函数暂停程序运行，同时等待键盘输入，返回类型永远是字符串
a = input()
b = input()

print('a + b = {} '.format(a + b))
