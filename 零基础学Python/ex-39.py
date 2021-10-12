# coding:utf8
# 文件操作 自带函数 open read readline seek write close
# 写入
# file1 = open("name.txt", 'w')
# file1.write('诸葛亮')
# file1.close()
# # 读取
# file2 = open("name.txt")
# print(file2.read())
# file2.close()
# # 新增
# file3 = open("name.txt", "a")
# file3.write("刘备")
# file3.close()
# 读取一行信息
# file4 = open("name.txt")
# print(file4.readline())
# # 读取多行信息并添加分隔符
# file5 = open("name.txt")
# for line in file5.readlines():
#     print(line)
#     print("----")
file6 = open('name.txt')
# 文件指针位置
print('当前文件指针位置%s' % file6.tell())
print('当前读取到了一个字符，字符的内容是 %s' % file6.read(1))
print('当前文件指针的位置%s' % file6.tell())
# seek参数，第1参数代表偏移量，第二参数 0 表示从文件开头偏移，1表示从当前位置偏移，2从文件结尾开始偏移
file6.seek(5, 0)
print('我们进行了seek操作')
print('当前文件指针位置%s' % file6.tell())
print('当前读取到了一个字符，字符的内容是 %s' % file6.read(1))
file6.close()