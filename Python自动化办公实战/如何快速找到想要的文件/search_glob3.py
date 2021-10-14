# -*- coding:utf8 -*-
# @Time：2021/10/14 2:34 下午
# @Author： Huang Jeff


import configparser
import pathlib
from pathlib import Path


def read_dirs(ini_filename, section, arg):
    """
    通过ini文件名，节和参数取得要操作的多个目录
    """
    current_path = pathlib.PurePath(__file__).parent
    inifile = current_path.joinpath(ini_filename)

    # cf是类ConfigParser的实例
    cf = configparser.ConfigParser()

    # 读取.ini文件
    cf.read(inifile)

    # 读取word节 和 searchpath参数
    return cf.get(section, arg).split(",")


def locate_file(base_dir, keywords='**/*'):
    p = Path(base_dir)
    # files = p.glob(keywords)
    # return list(files)
    return p.glob(keywords)

def write_to_db():
    """
        写入索引文件
    """
    current_path = pathlib.PurePath(__file__).parent
    dbfile = current_path.joinpath("search.db")

    with open(dbfile, 'w', encoding='utf-8') as f:
        for r in result:
            f.write(f"{str(r)}\n")


# 读取配置文件
dirs = read_dirs('search.ini', 'work', 'searchpath')

# 遍历目录
result = []
for dir in dirs:
    for files in locate_file(dir):
        result.append(files)

# 将目录写入索引文件
write_to_db()
