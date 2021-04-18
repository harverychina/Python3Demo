# coding:utf8
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Teacher(Person):
    def __init__(self, name, gender, course):

        super(Teacher, self).__init__(name, course)
        self.course = course


teacher1 = Teacher("tom", "man", "computer")
print("Teacher:{}，Course:{}".format(teacher1.name, teacher1.course))
