# coding:utf8

class Person(object):
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name):
        super(Student, self).__init__(name)
        self.name = name


class Teacher(Person):
    def __init__(self, name):
        (Teacher, self).__init__(name)
        self.name = name


class SkillMixin(object):
    def __init__(self, skill):
        self.skill = skill


class BasketBallMixin(SkillMixin, Student):
    def __init__(self, name, skill):
        super(self, BasketBallMixin).__init__(name, skill)


BasketBallMixin.Skill = '蓝球'
Student.name = '小王'
print("我是会打%s的学生，我叫%s" % (BasketBallMixin.Skill, Student.name))
BasketBallMixin.Skill = '足球'
Teacher.name = '张老师'
print("我是会打%s的老师，我是%s" % (BasketBallMixin.Skill, Teacher.name))
