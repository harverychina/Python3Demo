# coding:utf8
# 自定义上下文管理器
# 旧的写法
fd = open('name.txt')
try:
    for line in fd:
        print(line)
finally:
    fd.close()

# 新的写法，即是上下文管理器
with open('name.txt') as f:
    for line in f:
        print(line)
