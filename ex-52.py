# coding:utf8
# 装饰器的使用,普通装饰器不带参数使用方面不优雅
# 装饰器是怎么带参数的呢？
def new_tips(argv):
    def tips(func):
      def nei(a, b):
        # print('start')
        # 全局魔术方法 __name__
        print('start %s %s' %(argv, func.__name__))
        func(a, b)
        print('stop')
      return nei
    return tips

# @tips
@new_tips('add_module')
def add(a, b):
  print(a + b)

# @tips
@new_tips('sub_module')
def sub(a, b):
  print(a - b)


# print(add(1, 2))
# print(sub(1, 2))
print(add(4, 5))
print(sub(8, 1))