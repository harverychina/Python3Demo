# coding: utf-8
# while 语句 循环语句
num = 5
# while True:
#     print('a')
#     num = num + 1
#
#     if num > 10:
#         break

import time

while True:
    num = num + 1

    if num == 10:
        continue  # 当num等于10时，跳过本次循环不输出num的值

    print(num)
    time.sleep(1)
