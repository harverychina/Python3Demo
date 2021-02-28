# coding:utf8
# 函数闭包、 装饰器
# 闭包定义1
def func():
  a = 1
  b = 2
  return (a + b)

def sum(a):
  def add(b):
    return a + b
  return add
# add 函数名称或函数的引用
# add() 函数的调用

num1 = func()

num2 = sum(2)
print(num2(4))

# print(type(num1))
# print(type(num2))