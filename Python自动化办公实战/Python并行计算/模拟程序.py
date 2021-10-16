# -*- coding:utf8 -*-
# @Time：2021/10/16 8:10 上午
# @Author： Huang Jeff

from multiprocessing import Pool
# 1-100平方模拟程序


def f(x):
    # 计算平方
    return x * x


def test():
    with Pool(8) as p:
        res = p.map(f, range(1, 101))
        print(f'计算平方的结果是:{res}')


if __name__ == '__main__':
    test()
