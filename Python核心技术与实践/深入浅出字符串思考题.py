# -*- coding:utf8 -*-
# @Time：2021/11/9 10:13 上午
# @Author： Huang Jeff

import time
start_time = time.perf_counter()
s = " ".join(map(str, range(0, 1000)))
end_time = time.perf_counter()
print(end_time - start_time)


start_time = time.process_time()
s = ''
for n in range(0, 1000):
    s += str(n)
end_time = time.perf_counter()
print(end_time - start_time)


start_time = time.perf_counter()
l = []
for n in range(0, 1000):
    l.append(str(n))

s = ' '.join(l)
end_time = time.perf_counter()
print(end_time - start_time)
