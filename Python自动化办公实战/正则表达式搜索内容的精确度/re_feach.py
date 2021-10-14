# -*- coding:utf8 -*-
# @Time：2021/10/14 9:57 上午
# @Author： Huang Jeff
import re

# 查询11位手机号码
print(re.search("[0-9]{11}", "13800138000"))

# 模糊查询，搜索任意5个字符
# print(re.search(".....", "aaa1385557890bbb"))
print(re.search(".{5}", "aaa1385557890bbb"))
# 实现匹配5个字符
print(re.search("＾.....$", "aaa1385557890bbb"))

# 匹配电话号码
print(re.search("[0-9]{3}-[0-9]{8}", "我的电话号码：010-12345678。").group(0))

# 将内容中含有yes字样改为no
print(re.sub("(Y|y)(es)*", "No", "aayesbb"))
