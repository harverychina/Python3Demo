# coding:utf8
# 读取人物名称
# f = open("name2.txt")
# data = f.read()
# print(data.split('|'))

# 读取兵器名称
# f2 = open("name3.txt")
# i = 1
# for line in f2.readlines():
#   if i % 2 == 1:
#     # 去除换行和空行
#     print(line.strip('\n'))
#   i += 1

# f3 = open('sanguo.txt', encoding='utf8')
f3 = open('sanguo.txt')
print(f3.read().replace('\n',''))
