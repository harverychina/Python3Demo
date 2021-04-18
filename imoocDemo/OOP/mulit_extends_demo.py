class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):
    def __init__(self, name, gender, course):
        super(Student, self).__init__(name, gender)
        self.course = course


class Teacher(Person):
    def __init__(self, name, gender, subject):
        super(Teacher, self).__init__(name, gender)
        self.subject = subject


class SkillMixin(object):
    def __init__(self, skillSport):
        self.skillSport = skillSport


class BasketballMixin(Student, SkillMixin):
    def __init__(self, skillSport, name, gender, course):
        super(self, BasketballMixin).__init__(skillSport, name, gender, course)


class FootballMixin(Teacher, SkillMixin):
    def __init__(self, skillSport, name, gender, subject):
        super(
            self,
            BasketballMixin).__init__(
            skillSport,
            name,
            gender,
            subject)


BasketballMixin.skillSport = '篮球'
FootballMixin.skillSport = '足球'
Student.name = '刘学生'
Teacher.name = '陈老师'
print("我是会打%s的%s" % (BasketballMixin.skillSport, Student.name))
print("我是会打%s的%s" % (FootballMixin.skillSport, Teacher.name))
