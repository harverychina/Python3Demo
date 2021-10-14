# -*- coding:utf8 -*-
# @Time：2021/10/14 2:06 下午
# @Author： Huang Jeff


from pathlib import Path

base_dir = '/Users/huangjiancong/Desktop/Python3Demo/Python自动化办公实战/'
keywords = '**/*BBC*'
# 遍历base_dir指向的目录下所有的文件
p = Path(base_dir)

# 当前目录下包含BBC的所有文件名称
files = p.glob(keywords)
# files的类型是迭代器
# 通过list()函数转换为列表输出
# print(list(files))

# xlsx的结尾的文件
files2 = p.rglob('*.xlsx')
print(list(files2))

# 遍历子目录和所有文件
files3 = p.glob('**/*')
print(list(files3))
