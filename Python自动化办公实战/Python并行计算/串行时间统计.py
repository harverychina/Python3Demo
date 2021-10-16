# -*- coding:utf8 -*-
# @Time：2021/10/16 9:08 上午
# @Author： Huang Jeff

import time


def f(x):
    return x * x


def test():
    list1 = []

    time1 = time.time()
    for i in range(1, 10001):
        list1.append(f(i))
    time2 = time.time()

    print(str(time2 - time1))


if __name__ == '__main__':
    test()
