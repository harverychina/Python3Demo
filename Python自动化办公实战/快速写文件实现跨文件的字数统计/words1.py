# -*- coding:utf8 -*-
# @Time：2021/10/14 9:08 上午
# @Author： Huang Jeff

import pathlib

file_name = "e.txt"
file_number = 0

# 取得脚本所在目录
current_path = pathlib.PurePath(__file__).parent

# 和脚本同目录下的文件绝对路径
file = current_path.joinpath(file_name)

# 打开文件
with open(file, encoding='utf8') as f:
    # 读取文件
    content = f.read()
    words = content.rstrip()  # 去除右边空格
    file_number = len(words)   # 统计字数
    # print(number)

# 将结果写入文件里
file2 = "total.txt"
with open(file2, "w", encoding='utf8') as f:
    f.write(str(file_number) + "个字")
