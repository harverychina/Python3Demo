# -*- coding:utf8 -*-
# @Time：2021/12/23 9:33 AM
# @Author： Huang Jeff

import sys

a = []

print(sys.getrefcount(a))


def func(a):
    print(sys.getrefcount(a))


if __name__ == "__main__":
    func(a)
    print(sys.getrefcount(a))
