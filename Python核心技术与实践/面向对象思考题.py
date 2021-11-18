# -*- coding:utf8 -*-
# @Time：2021/11/18 10:18 上午
# @Author： Huang Jeff

"""
思考题：我们使用单一继承的时候，构造函数的执行顺序很好确定，即子类 -> 父类 -> 爷类 ->… 的链式关系。
"""


class A():
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")


class C(A):
    def __init__(self):
        print("C")


class D(B, C):
    def __init__(self):
        print("D")


if __name__ == "__main__":
    d = D()
