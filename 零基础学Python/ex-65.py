# coding:utf-8

# import time
# print(time.time())
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))


import datetime
# 当前时间
print(datetime.datetime.now())
# 10分钟以后的时间
newtime = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + newtime)
# 获取指定日期过了几天后的日期
one_day = datetime.datetime(2008, 5, 27)
new_date = datetime.timedelta(days=10)
print(one_day + new_date)
