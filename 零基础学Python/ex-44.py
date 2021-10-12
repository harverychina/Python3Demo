# coding:utf8
# 函数的变量的作用域
var1 = 123 # 外部变量

def func():
  # var1 = 456   # 内部变量，非全局变量
  global var1
  var1 = 456 # 全局变量
  print(var1)

func()
print(var1)