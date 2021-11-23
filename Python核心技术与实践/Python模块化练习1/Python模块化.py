# -*- coding:utf8 -*-
# @Time：2021/11/23 9:23 上午
# @Author： Huang Jeff

from utils import get_sum
from class_utils import *

print(get_sum(1, 2))

encoder = Encoder()
decoder = Decoder()

print(encoder.encode('abcde'))
print(decoder.decode('edcba'))
