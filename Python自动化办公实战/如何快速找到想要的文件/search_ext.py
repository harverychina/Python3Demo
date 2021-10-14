# -*- coding:utf8 -*-
# @Time：2021/10/14 2:54 下午
# @Author： Huang Jeff
import pathlib

# 获取索引文件路径
current_path = pathlib.PurePath(__file__).parent
dbfile = current_path.joinpath("search.db")


# 查询扩展为jpg的文件
def search_ext(file_ext):
    with open(dbfile, encoding='utf-8') as f:
        for line in f.readlines():
            if line.rstrip().endswith(file_ext):
                print(line.rstrip())


if __name__ == "__main__":
    search_ext('.jpg')
