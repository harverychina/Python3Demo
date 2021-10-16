# -*- coding:utf8 -*-
# @Time：2021/10/16 10:28 上午
# @Author： Huang Jeff

time_demo =[
    "8:20:40",
    "18:50:55",
    "10:50:10",
    "22:30:00"
]

for tt in time_demo:
    # 拆分时间，时，分，秒
    hour, minute, second = tt.split(":")

    if len(hour) == 1:
        new_hour = '0'+hour
    else:
        new_hour = hour

    minute = "{:>02d}".format(int(minute))
    second = "{:>02d}".format(int(second))

    new_time = [str(new_hour), str(minute), str(second)]
    new_time = ":".join(new_time)

    print(new_time)