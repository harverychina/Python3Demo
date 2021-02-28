# coding:utf-8
dict1 = {'abc': 456}
print(dict1)
dict2 = {'name': 'jack', 'age': 7, 'class': 'first'}
print(dict2['name'], dict2['age'])
# print(dict2['tow'])   # 不存在的键位
dict2['name'] = 'Rose'
print(dict2['name'])
# dict2.clear()            # 清空字典
# del dict2['name']       # 删除字典
# print(dict2)
# copy 和赋值的区别
dict3 = dict1             # 浅拷贝：引用对象
dict4 = dict1.copy()      # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用

dict1['abc'] = 'def'

print(dict1)
print(dict3)
print(dict4)
