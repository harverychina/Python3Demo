# -*- coding:utf8 -*-
# @Time：2021/11/3 2:43 下午
# @Author： Huang Jeff

# Python的字符串是不可变的，因此想修改则需要创建的字符串来完成

s = 'hello'
# s[0] = 'H'  # 报错 'str' object does not support item assignment

# s = 'H' + s[1:]  # 创建一个新字符串
# print(s)
# 采用replace函数完成
# s = s.replace('h', 'H')
# print(s)

s += 'H'
print(s)

def query_data(namespace, table):
    """
    given namespace and table, query database to get corresponding data
    """
    return namespace, table

path = 'hive://ads/training_table'
# 从//开始截取字符串后的内容，然后分割/前、后面的两部分，要第一部分
namespace = path.split('//')[1].split('/')[0]
# 从//开始截取字符串后的内容，然后分割/前、后面的两部分，要第二部分
table = path.split('//')[1].split('/')[1]
data = query_data(namespace, table)
print(data)

# 去掉首尾、去开头，去尾部的 字符串

s = ' my name is jason  '
s.strip()
print(s)

sub = 'jason'
print(s.find(sub)) # 查到显示第子符串开始位置，如果找不到则显示-1

# 格式化format函数
id = '123'
name = 'jason'
print('no data available for person with id: {}, name: {}'.format(id, name))

print('no data available for person with id: %s, name: %s' % (id, name))
