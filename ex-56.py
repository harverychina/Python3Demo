# coding:utf8
# 集合，值不重复
a = {1, 2, 2, 3, 4}
print(type(a))
# 将集合转换列表，重复元素不存在列表当中
print(a)
a = list(a)
print(a[2])

# condition = False
condition = True
# 表达式不管如何左边是1就代表真，右边的if表达式是当值是真则是1，与左边表达式成并且运算
x = 1 if condition else 0
print(x)
