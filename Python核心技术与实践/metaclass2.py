# -*- coding:utf8 -*-
# @Time：2021/12/8 10:21 AM
# @Author： Huang Jeff

# 正常定义
class MyClass:
    data = 1


instance = MyClass()

print(MyClass, instance)
print(instance.data)

# 手工调用type运算符
MyClass = type('MyClass', (), {'data': 1})
instance = MyClass()
print(instance, MyClass)
print(instance.data)
