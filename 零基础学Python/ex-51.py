# coding:utf8
# 装饰器定义
# 引用 time库
import time


# 装饰器定义写法，类似闭包写法
def timmer(func):
  def wrapper():
    start_time = time.time()
    func()
    stop_time = time.time()
    print('运行时间是%s秒' % (stop_time - start_time))
  return wrapper

# print(time.time())

# time.sleep(3)
@timmer
def i_can_sleep():
  time.sleep(3)

# start_time = time.time()
i_can_sleep()
# stop_time = time.time()
# print('程序运行了 %s秒' %(stop_time - start_time))