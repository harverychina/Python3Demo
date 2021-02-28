# coding:utf-8
# 集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 去除内容重复
print('orange' in basket)
print('crabrass' in basket)
# 使用set创建集合
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)  # 集合a中包含而集合b中不包含的元素
print(b - a)  # 集合b中包含而集合a中不包含的元素
print(a | b)  # 集合a和b中都包含了的元素
print(a & b)  # 集合a和b中都包含了的元素
print(a ^ b)  # 不同时包含a和b的元素
