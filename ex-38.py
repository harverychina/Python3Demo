# coding: utf8
# for 循环的另一种方式：列表推导式
# 从 1 到 10 所有偶数的平方
alist = []
for i in range(1, 11):
    if (i % 2 == 0):
        alist.append(i * i)

print(alist)
# 简洁写法：列表推导式
blist = [i * i for i in range(1, 11) if (i % 2) == 0]
print(blist)
# 简洁写法：字典推导式Ò
z_num = {}
for i in zodiac_name:
    z_num[i] = 0
z_num = {i: 0 for i in zodiac_name}
