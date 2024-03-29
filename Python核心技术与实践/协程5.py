# -*- coding:utf8 -*-
# @Time：2021/12/15 1:50 PM
# @Author： Huang Jeff

import asyncio
import time


async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')


async def main():
    print('before await')
    await worker_1()
    print('awaited worker_1')
    await worker_2()
    print('awaited worker_2')

if __name__ == "__main__":
    start = time.perf_counter()
    print(asyncio.run(main()))
    end = time.perf_counter()
    print("耗时: {:.2f}s".format(end - start))
