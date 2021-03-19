# coding:utf8
"""
正则表达式实例
"""

import re
# 匹配任意三个字符
# p = re.compile('...')
# print(p.match('bat'))
# 任意字符出现3次
# p = re.compile('.{3}')
# print(p.match('bat'))
# 匹配年月日
# p = re.compile('....-..-..')
# p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.match('2021-03-19'))
# r 原样输出
# print(r'\nx\n')
p = re.compile(r'(\d+)-(\d+)-(\d+)')
# 取出括号里面的内容，1 代表第一个
# print(p.match('2021-03-19').group(1))
# 分组单个取出内容
print(p.match('2019-05-10').group(2))
# 全部取出 groups()
print(p.match('2019-05-10').groups())
# 全部取出赋值给变量
year, month, day = p.match('2018-05-10').groups()
print(year)
