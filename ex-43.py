# coding:utf8
# 函数的可变长参数

# print('abc', end='\n')
# print('abc')

# def func(a, b, c):
#   print('a = %s' % a)
#   print('b = %s' % b)
#   print('c = %s' % c)
#
# func(1, c=3, b=2)

# 取得参数的个数
def howlong(first, *other):
  print(1 + len(other))

howlong(123, 456)
