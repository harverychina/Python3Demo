# coding:utf8
# 闭包的使用
# 直线公式 a*x + b
# def a_line(a, b):
#   def age_x(x):
#     return a * x + b
#   return age_x
# lambda写法
def a_line(a, b):
    return lambda x: a * x + b


# a = 3 b =5
# x = 10
line1 = a_line(3, 6)
print(line1(10))
