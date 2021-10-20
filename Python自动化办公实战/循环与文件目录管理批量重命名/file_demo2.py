# -*- coding:utf8 -*-
# @Time：2021/10/19 10:38 上午
# @Author： Huang Jeff

import os
import argparse


def rename(file_path, old_ext):
    """ 批量改名函数 """
    print(old_ext)
    old_names = os.listdir(file_path)
    new_name = 1

    for old_name in old_names:

        if old_name.endswith(old_ext):

            old_path = os.path.join(file_path, old_name)
            new_path = os.path.join(file_path, str(new_name) + ".JPG")
            os.rename(old_path, new_path)
            new_name = int(new_name) + 1


def args_opt():
    # 定义参数对象
    parser = argparse.ArgumentParser()
    # 增加参数选项、是否必须、帮助信息
    parser.add_argument("-p", "--path", required=True, help="path to rename")
    parser.add_argument("-e", "--ext",  required=True, help="files name extension, eg: jpg")

    # 返回取得的所有参数
    return parser.parse_args()


if __name__ == "__main__":
    args = args_opt()
    rename(args.path, "." + args.ext)
    print(os.listdir(args.path))

# python3 rename_v2.py -p /Users/edz/Desktop/pic -e jpg
