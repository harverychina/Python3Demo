# coding="utf8";
# 面向过程编程
# user1 = {'name': 'tom', 'hp': 100}
# user2 = {'name': 'jerry', 'hp': 80}
#
#
# def print_role(rolename):
#     print('name is %s, hp is %s' % (rolename['name'], rolename['hp']))
#
#
# print_role(user1)


# 面向对象编程
class Player():  # 定义一个类
    def __init__(self, name, hp, occu):  # 初始化方法
        self.__name = name  # 变量被称作属性  类的封装 该name变量不能被实例进行修改
        self.hp = hp
        self.occu = occu

    def print_role(self):  # 定义一个方法
        print('%s: %s %s' % (self.__name, self.hp, self.occu))

    def updateName(self, newname):
        self.name = newname


class Monster():
    '定义怪物类'
    pass


user1 = Player('tom', 100, 'war')
user2 = Player('jerry', 100, 'master')
user1.print_role()
user2.print_role()
# 修改类的name属性，但对__name属性前有两个下划线是无法进行修改的。
user1.updateName('wilson')
user1.print_role()
