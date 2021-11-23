# -*- coding:utf8 -*-
# @Time：2021/11/23 9:33 上午
# @Author： Huang Jeff
class Encoder(object):
    def encode(self, s):
        return s[::-1]


class Decoder(object):
    def decode(self, s):
        return ''.join(reversed(list(s)))
