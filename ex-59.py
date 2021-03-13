# coding:utf8
# 多线编程 thread

import threading
import time
from threading import current_thread


def myThread(arg1, arg2):
    # 获取线程的名称 和 线程开始注释
    print(current_thread().getName(), 'start')
    print('%s %s' % (arg1, arg2))
    time.sleep(1)
    # 获取线程的名称 和 线程结束注释
    print(current_thread().getName(), 'stop')




for i in range(1, 6, 1):
    # t1 = myThread(1, i + 1)
    t1 = threading.Thread(target=myThread, args=(i, i + 1))
    t1.start()

# 获取线程的名称 和 主线程结束注释
print(current_thread().getName(), 'end')

