
# coding: utf8
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog = Animal("Tom", 3)
cat = Animal("Jack", 2)


print(dog.name)
print(dog.age)
print(cat.name)
print(cat.age)
