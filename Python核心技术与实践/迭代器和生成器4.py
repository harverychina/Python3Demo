# -*- coding:utf8 -*-
# @Time：2021/12/14 9:56 AM
# @Author： Huang Jeff

# 贪心算法

def is_subsequence(a, b):
    b = iter(b)
    return all(i in b for i in a)


print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))


b = (i for i in range(5))

print(2 in b)
print(3 in b)
print(4 in b)
print(6 in b)
