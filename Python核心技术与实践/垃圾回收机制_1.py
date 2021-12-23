# -*- coding:utf8 -*-
# @Time：2021/12/23 8:51 AM
# @Author： Huang Jeff

import os
import sys

import objgraph as objgraph
import psutil
import gc


# 显示当前 python 程序占用内在大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} 内存使用了: {} MB'.format(hint, memory))


def func():
    show_memory_info("局部变量初始化")
    a = [i for i in range(10000000)]
    show_memory_info("局部变量创建后")
    return a


def func2():
    show_memory_info("全局变量初始化")
    global a
    a = [i for i in range(10000000)]
    show_memory_info("全局变量创建后")


# python内部引用计数
def jishu():
    a = []
    print(sys.getrefcount(a))

    def func(a):
        print(sys.getrefcount(a))

    func(a)
    print(sys.getrefcount(a))


# 循环引用
def func3():
    show_memory_info("循环引用初始化")
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    show_memory_info("ab创建完成")
    a.append(b)
    b.append(a)


if __name__ == "__main__":
    func()
    func2()
    show_memory_info('finished')
    # 手动回收
    show_memory_info("局部变量初始化")
    a = [i for i in range(1000000)]
    show_memory_info("局部变量创建后")
    del a
    gc.collect()
    # print(a)
    # 循环引用
    func3()
    show_memory_info("循环引用完成")
    gc.collect()
    show_memory_info("手动垃圾回收完成")

    # objgraph
    a = [1, 2, 3]
    b = [4, 5, 6]

    a.append(b)
    b.append(a)

    objgraph.show_refs([a], filename=" /Users/huangjiancong/Desktop/Python3Demo/Python核心技术与实践/objref.png")
    objgraph.show_backrefs([a], filename=" /Users/huangjiancong/Desktop/Python3Demo/Python核心技术与实践/backref.png")
