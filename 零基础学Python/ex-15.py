# coding:utf-8
# 使用空格分隔输入的数字成为新的列表
# lis = list(map(int, input().split()))
# 使用逗号分隔输入的内容为新的列表，注意map后面的类型
lis = list(map(str, input().split(',')))
print(lis)