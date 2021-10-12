# coding:utf-8

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# input方法
year = int(input('请用户输入出生年份'))

if chinese_zodiac[year % 12] == '狗':
    print('狗年出生')
