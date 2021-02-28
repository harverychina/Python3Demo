# coding:utf8
# 内置函数 filter()  map()  reduce()  zip()
# 大于 2 值
a = [1, 2, 3, 4, 5, 6, 7]
# list(filter(lambda x: x > 2, a))

a = [1, 2, 3]
# 列表元素逐一加1
list(map(lambda x: x + 1, a))
# 列表a和b元素依次相加
b = [5, 6, 7]
list(map(lambda x, y: x + y, a, b))
# 使用reduce()之前，需要使用" from functools import reduce "

from functools import reduce
# 两个元素依次相加，列表元素依次与某个整数相加
reduce(lambda x, y: x + y, [2, 3, 4], 1)
# (((1+2)+3)+4)

# 元组合并
# (1,2,3),(4,5,6)
# for i in zip((1,2,3),(4,5,6)):
#   print(i)

# 字典的key和value的对调
dicta = {'a':'aa','b':'bb'}
dictb = zip(dicta.values(), dicta.keys())
print(dict(dictb))

