# -*- coding:utf8 -*-
# @Time：2021/11/23 9:37 上午
# @Author： Huang Jeff

import sys
sys.path.append("../..")

from utils.class_utils import *

encoder = Encoder()
decoder = Decoder()

print(encoder.encoder('abcde'))
print(decoder.decoder('edcba'))
