# coding: utf8
class Animal(object):
    def __init__(self, name, age, localtion):
        self.__name = name
        self.__age = age
        self.__location = localtion

    def get_all_values(self):
        return "name:{}, age:{},localtion:{}".format(self.__name, self.__age, self.__location)


cat = Animal('tom', 3, "USA")
print(cat.get_all_values())
