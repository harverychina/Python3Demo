# -*- coding:utf8 -*-
# @Time：2021/12/14 9:15 AM
# @Author： Huang Jeff
import functools
import os
import time

import psutil


# 生成器
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print("函数{}运行耗时{}秒".format(func.__name__, end-start))
        return res
    return wrapper


@log_execution_time
def test_iterator():
    show_memory_info('initing iterator')
    list_1 = [i for i in range(100000000)]
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    show_memory_info('after sum called')


@log_execution_time
def test_generator():
    show_memory_info('initing iterator')
    list_2 = (i for i in range(100000000))
    show_memory_info('after generator initiated')
    print(sum(list_2))
    show_memory_info('after sum called')


test_iterator()
test_generator()
