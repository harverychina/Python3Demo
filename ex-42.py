# coding:utf8
# 函数，函数参数
# def func(filename):
#   print(open(filename).read())
#   print('text func')
#
# func('name.txt')
import re
# 统计主角名字在小说中出现的次数
def find_item(hero):
  with open("sanguo.txt") as f:
    data = f.read().replace("\n", "")
    # 统计
    name_num = re.findall(hero, data)
    print('主角 %s 出现 %s 次' %(hero, len(name_num)))
  return name_num

# 读取人物信息
name_dict = {}
with open("name2.txt") as f:
  for line in f:
    names = line.split("|")
    for n in names:
      # print(n)
      # 调用自定义的统计函数 find_item
      name_num = find_item(n)
      name_dict[n] = name_num

# 对统计数据进行排序，并且出现前10位
name_sort = sorted(name_dict.items(), key = lambda item: item[1], reverse=True)
print(name_sort[0:10])