# -*- coding:utf8 -*-
# @Time：2021/10/15 2:03 下午
# @Author： Huang Jeff

sorted_list = sorted([30, 50, 20, 10, 40])
print(sorted_list)

# 既包含字符串又包含数字的列表，进行排序操作的时候，你需要先统一类型，把数字使用 str() 函数转换为字符串类型，再对列表进行排序。
sorted_list2 = sorted(['A', str(1), "bb"])
print(sorted_list2)

"""sort() 函数和 sorted() 函数的区别
1. sorted() 函数不会对原有的列表进行修改，它会把排序好的结果存入到一个新的列表当中
2. sort() 函数使用的方式是“列表.sort()”格式
3. sort() 函数是列表数据类型自带的，所以只能对列表数据类型进行排序，不能对其他数据类型排序，但 sorted() 函数可以支持任何可迭代的对象。
4. sorted() 第二参数"iterable"对象，表示只要该对象可迭代，sorted()函数就能对它进行排序
"""
list3 = ["a", "c", "bb"]
no_value = list3.sort()
print(list3)
# 因为sort()函数是对列表进行原地修改，所以返回为none
print(no_value)

# sorted函数第四参数，自定义排序
sorted_list4 = sorted([30, 50, 20, 10, 40], reverse=True)
print(sorted_list4[:3])

