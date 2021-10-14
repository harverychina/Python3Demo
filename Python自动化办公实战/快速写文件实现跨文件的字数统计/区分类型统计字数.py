# -*- coding:utf8 -*-
# @Time：2021/10/14 9:31 上午
# @Author： Huang Jeff

import string
# 英文、数字、空格、中文、特殊字符进行分类统计
word_count = {
    "count_en": [],
    "count_dg": [],
    "count_sp": [],
    "count_zh": [],
    "count_pu": []
}


def str_count(str):
    # 找出字符串的中英文、空格、数字、标点符号个数
    count_en = count_dg = count_sp = count_zh = count_pu = 0

    for s in str:
        if s in string.ascii_letters:
            count_en += 1
        elif s.isdigit():
            count_dg += 1
        elif s.isspace():
            count_sp += 1
        elif s.isalpha():
            count_zh += 1
        else:
            count_pu += 1
    print('英文字符：', count_en)
    print('数字：', count_dg)
    print('空格：', count_sp)
    print('中文：', count_zh)
    print('特殊字符：', count_pu)

    word_count["count_en"].append(count_en)
    word_count["count_dg"].append(count_dg)
    word_count["count_sp"].append(count_sp)
    word_count["count_zh"].append(count_zh)
    word_count["count_pu"].append(count_pu)


str_count("'中文：', count_zh")
# str_count("'特殊字符：', count_pu")
for item in word_count:
    print(f"{item} 数量为：{sum(word_count[item])}")
