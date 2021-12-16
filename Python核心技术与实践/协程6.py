# -*- coding:utf8 -*-
# @Time：2021/12/16 9:14 AM
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
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print('before await')
    await task1
    print('awaited work_1')
    await task2
    print('awaited work_2')

if __name__ == "__main__":
    start = time.perf_counter()
    print(asyncio.run(main()))
    end = time.perf_counter()
    print("耗时:{:.2f}".format(end - start))
