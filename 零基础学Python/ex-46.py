# coding:utf8
# lambad 表达式
# 函数的简化写法，更清晰
# def true(): return True
# lambda : True

# lamba写法
# lambda x:x<=(month, day)
# 函数写法
# def func(x):
  # return x <= (month, day)

# lamba写法
lambda item:item[1]
# 函数写法  取出字典每个元素的value值
def func2(item):
  return item[1]

# 举例说明
adict = {'a':'aa', 'b':'bb'}
for i in adict.items():
  print(func2(i))
