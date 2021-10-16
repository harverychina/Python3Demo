# -*- coding:utf8 -*-
# @Time：2021/10/16 8:56 上午
# @Author： Huang Jeff

from multiprocessing import Pool
import os
import time


def f(x):
    return x * x


def test():

    with Pool(4) as p:
        # 并行计算
        time1 = time.time()
        res = p.map(f, range(1, 10001))
        time2 = time.time()
        print(f'计算平方的结果是:{res}')
    print(str(time2 - time1))


if __name__ == 'main':
    test()
