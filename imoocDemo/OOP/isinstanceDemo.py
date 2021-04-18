# coding: utf8
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course


p = Person("tim", "male")
s = Student("bob", "male", 88)
t = Teacher("alice", "female", "English")

print(isinstance(t, Person))     # True
print(isinstance(t, Student))    # False
print(isinstance(t, Teacher))    # True
print(isinstance(t, object))     # True
