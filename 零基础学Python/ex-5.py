# coding: utf-8
# 偶数之和、奇数之和
a = [1, 2, 3, 4, 5, 6]
# s = sum([num for num in a if num % 2 == 0])
s = sum([num for num in a if num % 2 != 0])
print(s)