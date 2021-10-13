# -*- coding:utf8 -*-
import jieba.posseg as psg
words1 = "速度快，包装好，看着特别好，喝着肯定不错！价廉物美"
words5 = [(w.word, w.flag) for w in psg.cut(words1)]


