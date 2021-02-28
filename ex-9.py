# codig:utf-8
# 利用循环语句创建有序列的列表
lst1 = [i for i in range(0, 10)]
print(lst1)

# 另外一种写法

lst2 = list(range(0, 10))
# print(list(range(0, 10)))
# 循环输出偶数列表
print([l for l in lst2 if l % 2 == 0])
