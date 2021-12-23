# -*- coding:utf8 -*-
# @Time：2021/12/23 8:31 AM
# @Author： Huang Jeff
import time
from threading import Thread


def CountDown(n):
    while n > 0:
        n -= 1


n = 100000000

t1 = Thread(target=CountDown, args=[n // 2])
t2 = Thread(target=CountDown, args=[n // 2])

starttime = time.perf_counter()

t1.start()
t2.start()
t1.join()
t2.join()

endtime = time.perf_counter()

print("用时：{:2f}s".format(endtime - starttime))
