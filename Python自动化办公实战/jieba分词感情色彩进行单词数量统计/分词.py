# -*- coding:utf8 -*-
import jieba

words1 = "速度快，包装好，看着特别好，喝着肯定不错！价廉物美"

word2 = jieba.cut(words1)

print("/".join(words2))
