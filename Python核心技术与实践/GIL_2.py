# -*- coding:utf8 -*-
# @Time：2021/12/23 8:44 AM
# @Author： Huang Jeff

import threading
n = 0
lock = threading.Lock() # 使用Lock工具，确保线程安全

def foo():
    global n
    n += 1  # 线程的不安全因素，容易被打断


threads = []
for i in range(100):
    t = threading.Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(n)

# 测试 n +=1 语句被打断的效果
# import dis
# print(dis.dis(foo))
