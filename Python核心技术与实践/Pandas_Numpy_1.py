# -*- coding:utf8 -*-
# @Time：2022/1/11 8:41 AM
# @Author： Huang Jeff
from os import path

import pandas as pd


def assert_msg(condition, msg):
    if not condition:
        raise Exception(msg)


def read_file(filename):
    # 获得文件绝对路径
    filepath = path.join(path.dirname(__file__), filename)

    # 判定文件是否存在
    assert_msg(path.exists(filepath), "文件不存在")

    # 读取CSV文件并返回
    return pd.read_csv(
        filepath,
        index_col=0,
        parse_dates=True,
        infer_datetime_format=True)


BTCUSD = read_file("/Users/huangjiancong/Desktop/Python3Demo/Python核心技术与实践/BTCUSD_GEMINI.csv")
assert_msg(BTCUSD.__len__() > 0, '读取失败')
print(BTCUSD.head())
