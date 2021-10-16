# -*- coding:utf8 -*-
# @Time：2021/10/16 10:19 上午
# @Author： Huang Jeff

"""
f-string 和 format() 函数都具有对字符串输出格式调整的功能，不过前者更适用于字符串和变量连接的场景，后者更适用于调整字符串的格式。此外，f-string 除了可以用来观察文字对齐的结果外，你还可以在输出变量的同时也输出字符串。
"""
string = "    广东省广州市     "
newstring = string.strip()
print(f"|{newstring}|")
