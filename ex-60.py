# coding:utf8
import threading
from threading import current_thread
# 继承和多态


class Mythead(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')


t1 = Mythead()
t1.start()
t1.join()

print(current_thread().getName(), 'end')
