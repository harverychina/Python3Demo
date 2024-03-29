# -*- coding:utf8 -*-
# @Time：2021/12/15 1:34 PM
# @Author： Huang Jeff

import asyncio
import time


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task

if __name__ == "__main__":
    start = time.perf_counter()
    print(asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4'])))
    end = time.perf_counter()
    print("耗时：{:.2f}s".format(end - start))
