# -*- coding:utf8 -*-
import jieba
words1 = "速度快，包装好，看着特别好，喝着肯定不错！价廉物美"
words2 = jieba.cut(words1)
words3 = list(words2)
print("/".join(words3))

stop_words = ["，", "！"]
words4 = [x for x in words3 if x not in stop_words]
print(words4)
