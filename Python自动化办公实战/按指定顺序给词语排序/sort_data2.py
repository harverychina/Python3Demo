# -*- coding:utf8 -*-
# @Time：2021/10/15 2:17 下午
# @Author： Huang Jeff


students = [('Tom', 'M', '1005'),
            ('Jerry', 'M', '1003'),
            ('shuke', 'M', '2003'),
            ('Beta', 'M', '2001')]
# 按人名首字母进行排序
print(sorted(students))

# 按学号进行排序
print(sorted(students, key=lambda s: s[2]))


def get_tuple_pos3(my_tuple):
    # 定义一个取得排序后第3位置元素
    return my_tuple[2]


print(get_tuple_pos3(('Jerry', 'M', '1003')))
print(sorted(students, key=get_tuple_pos3))

student_dict1 = {
    'Jerry': '1003',
    'Tom': '1005',
    'Beta': '2001',
    'Shuke': '2003'}

print(student_dict1.items())
# 按字典关健字排序
print(sorted(student_dict1.items(), key=lambda d: d[0]))
# 按学号进行排序
result = sorted(student_dict1.items(), key=lambda d: d[1])
print(result)
# 以字典形式输出结果
print(dict(result))
