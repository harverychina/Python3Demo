# coding: utf8

class Animal(object):
    count = 0
    # 私有变量
    # __count = 0

    def __init__(self, name, age):
        self.name = name
        # 私有变量 age
        self.__age = age
        # Animal.__count += 1
        Animal.count += 1
#     当子类需要获取父类的私有变量则需要在父类定义一个方法

    def get_age(self):
        return self.__age


cat = Animal("小花", 4)
# print(cat.__count)
print(cat.count)
# 子类不能直接访问父类的私有变量
# print(cat.__age)
print(cat.get_age())
dog = Animal("小猪", 3)
# print(dog.count)
