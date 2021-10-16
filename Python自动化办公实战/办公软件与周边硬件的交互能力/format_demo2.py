# -*- coding:utf8 -*-
# @Time：2021/10/16 10:04 上午
# @Author： Huang Jeff

date_demo = [
    "2021-03-18",
    "21-3-18",
    "2021-12-21",
    "2021-3-8",
    "21-3-1"
]

for dd in date_demo:
    # 折分日期，分年、月、日
    year, month, day = dd.split('-')

    # 调整格式，两位年份变成四位年份
    if len(year) == 2:
        new_year = 2021
    else:
        new_year = year

    month = "{:>02d}".format(int(month))
    day = "{:>02d}".format(int(day))

    # 合并日期
    new_date = [str(new_year), str(month), str(day)]
    new_date = "-".join(new_date)

    print(new_date)
