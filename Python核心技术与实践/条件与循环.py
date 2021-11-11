# -*- coding:utf8 -*-
# @Time：2021/11/10 10:09 上午
# @Author： Huang Jeff

# if id == 0:
#     print('red')
# elif id == 1:
#     print('yellow')
# else:
#     print('green')


# d = {'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}
#
# for k in d:
#     print(k)
#
# for v in d.values():
#     print(v)
#
# for k, v in d.items():
#     print('key :{}, value: {}'.format(k, v))


# l = [1, 2, 3, 4, 5, 6, 7]
# for index in range(0, len(l)):
#     if index < 5:
#         print(l[index])


"""
思考题:
给定下面两个列表 attributes 和 values，要求针对 values 中每一组子列表 value，
输出其和 attributes 中的键对应后的字典，最后返回字典组成的列表。
"""
attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
          ['mike', '1999-01-01', 'male'], ['nancy', '2001-02-01', 'female']]


# lis = []
# for i in values:
#     dic = {}
#     for n, j in enumerate(i):
#         dic[attributes[n]] = j
#     lis.append(dic)
#
# print(lis)

# lis = []
# for i in values:
#     print(i)
#     print(dict(zip(attributes, i)))
#     print(lis.append(dict(zip(attributes, i))))

print([dict(zip(attributes, i)) for i in values])
