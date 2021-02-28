# coding:utf-8
# 映射列表或类型转换整个列表
print(list(map(int, ['1', '2', '3'])))
# [1,2,3]
print(list(map(float, [1, 2, 3])))
# [1.0,2.0,3.0]
print([float(i) for i in [1, 2, 3]])
# [1.0,2.0,3.0]
