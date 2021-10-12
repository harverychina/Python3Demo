# coding:utf-8
# 字符串的定义和使用
# chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

year = 2021
print(year % 12)
print(chinese_zodiac[year % 12])

print('狗' not in chinese_zodiac)

print(chinese_zodiac + 'abcd')

print(chinese_zodiac * 3)