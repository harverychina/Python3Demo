# coding:utf-8
# 从1到20个数字当中找到以下情况：
# 用于将能被3整除又能被5整除的数字替代成为字符串‘FizzBuzz’
# 用于将能被3整除的数字替代成为字符串‘Fizz’
# 用于将能被5整除的数字替代成为字符串‘Buzz’

l = [
    'FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i %
    3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, 20)
]
print(l)