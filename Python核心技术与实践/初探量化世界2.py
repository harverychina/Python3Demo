# -*- coding:utf8 -*-
# @Time：2022/1/6 2:07 PM
# @Author： Huang Jeff

import matplotlib.pyplot as plt
import pandas as pd
import requests

# 选择要获取的数据时间段
periods = '3600'

# 通过Http抓取btc历史价格数据
resp = requests.get('https://api.cryptowat.ch/markets/gemini/btcusd/ohlc',
  params={
    'periods': periods
  })
data = resp.json()

# 转换成pandas data frame
df = pd.DataFrame(
  data['result'][periods],
  columns=[
    'CloseTime',
    'OpenPrice',
    'HighPrice',
    'LowPrice',
    'ClosePrice',
    'Volume',
    'NA'])

# 输出DataFrame的头部几行
print(df.head())

# 绘制btc价格曲线
df['ClosePrice'].plot(figsize=(14, 7))
plt.show()
