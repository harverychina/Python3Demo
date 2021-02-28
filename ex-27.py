# coding:utf-8
dict1 = {'name': 'jack', 'age': 7, 'class': 'two'}
# 判断键是否在字典
# print('two' in dict1)
# 遍历字典所有键和值
# print(dict1.items())
# 遍历字典的键
# print(dict1.keys())
# 可以使用list转换字典的键（方法比上面更好）
# print(list(dict1))
# 获取字典某个键值内容
# print(dict1.get('home', None))
# get 和 setdefault 当值不存在时，返回默认值有所不同
# get 和 setdefault 当值不存在时，get不会改变字典，而setdefault是添加新值
# print(dict1.setdefault('class1', 'one'))
# print(dict1)
# 当内容不在字典当时，需要添加默认值，如下所示，否则报错
# print(dict1.pop('class1'))
print(dict1.pop('class2', 'class2'))
