# -*- coding:utf8 -*-
# @Time：2021/12/15 10:00 AM
# @Author： Huang Jeff

# 爬虫例子引入协和和并发

import time

def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))


def main(urls):
    for url in urls:
        crawl_page(url)


if __name__ == "__main__":
    start = time.perf_counter()
    main(['url_1', 'url_2', 'url_3', 'url_4'])
    end = time.perf_counter()
    print("运行耗时：{:.2f}s".format(end - start))
