# coding:utf8
# 异常的检测和处理
# try:
#   i = j
# except Exception:
#   print('请定义变量')
# finally:

# try:
#   year = int(input('input year:'))
# except ValueError:
#   print('年份要输入数字')

# try:
#   a = 123
#   a.append()
# except AttributeError:
#   print('数字变量是无法使用添加属性！')

# 多种异常
# except(ValueError, AttributeError, KeyError)

# try:
#   print(1 / 0)
# except ZeroDivisionError as e:
#   print('0不能做除数 %s' % e)
# 全部异常
# try:
#   print(1 / 'a')
# except Exception as e:
#   print('类型不符合运算操作 %s' % e)
# 自定义异常
# try:
#   raise NameError('helloError')
# except NameError:
#   print('my custom error')

try:
  # a = open("name.txt")
  a = open("name1.txt")
except Exception as e:
  print(e)
finally:
  a.close()