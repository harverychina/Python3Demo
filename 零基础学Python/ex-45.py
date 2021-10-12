# coding:utf8
# 迭代器 iter() 与生成器 next()
# list1 = [1, 2, 3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) #except 异常 try catch

# for i in range(10, 20, 2):
#   print(i)

def frange(start, stop, step):
  x = start
  while x < stop:
    yield x   # 暂停，统计数据 使用 yield 函数
    x += step

for i in frange(10, 20, 0.5):
  print(i)
