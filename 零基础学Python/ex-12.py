# coding:utf-8
# 创建有序列化的集合Square，本例是创建0~10平方后偶数结果
s = {x**2 for x in range(10) if x % 2 == 0}
print(s)
# {0, 64, 4, 36, 16}