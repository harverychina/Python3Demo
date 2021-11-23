# -*- coding:utf8 -*-
# @Time：2021/11/23 9:40 上午
# @Author： Huang Jeff

from utils.class_utils import *
from utils.utils import *

if __name__ == "__main__":
    print(get_sum(1, 2))

    encoder = Encoder()
    decoder = Decoder()

    print(encoder.encode("abcde"))
    print(decoder.decode("edcda"))
