# -*- coding:utf8 -*-
# @Time：2021/12/16 10:35 AM
# @Author： Huang Jeff

import asyncio
import time


async def worker_1():
    await asyncio.sleep(1)
    return 1


async def worker_2():
    await asyncio.sleep(2)
    return 2 / 0


async def worker_3():
    await asyncio.sleep(3)
    return 3


async def main():
    task_1 = asyncio.create_task(worker_1())
    task_2 = asyncio.create_task(worker_2())
    task_3 = asyncio.create_task(worker_3())

    await asyncio.sleep(2)
    task_3.cancel()

    res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
    print(res)


if __name__ == "__main__":
    start = time.perf_counter()
    print(asyncio.run(main()))
    end = time.perf_counter()
    print("耗时:{:.2f}".format(end - start))
