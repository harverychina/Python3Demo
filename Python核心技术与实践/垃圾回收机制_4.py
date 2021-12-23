# -*- coding:utf8 -*-
# @Time：2021/12/23 10:07 AM
# @Author： Huang Jeff

import objgraph

a = [1, 2, 3]
b = [4, 5, 6]

a.append(b)
a.append(a)

objgraph.show_refs([a])
