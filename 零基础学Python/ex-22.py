# coding:utf-8
# 质数是一个只能被自身和1整除的数。例如:2、3、5、7等。
print(list(filter(lambda x:all(x % y != 0 for y in range(2,x)), range(2,13))))
