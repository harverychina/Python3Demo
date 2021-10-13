# -*- coding:utf8 -*-
import jieba.posseg as psg
words1 = "速度快，包装好，看着特别好，喝着肯定不错！价廉物美"
words5 = [(w.word, w.flag) for w in psg.cut(words1)]

# 保留形容词
saved = ['a', ]
words5 = [x for x in words5 if x not in saved]
print(words5)
