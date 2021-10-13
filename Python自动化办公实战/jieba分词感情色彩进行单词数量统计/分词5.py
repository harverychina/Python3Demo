# -*- coding:utf8 -*-
# @Time：2021/10/13 2:32 下午
# @Author： Huang Jeff
import jieba
import jieba.posseg as psg
from snownlp import SnowNLP
# words1 = "速度快，包装好，看着特别好，喝着肯定不错！价廉物美"
words1 = "速度慢，包装不好，看着特别不好，喝着肯定很差！"
words2 = jieba.cut(words1)
words3 = list(words2)
words5 = [(w.word, w.flag) for w in psg.cut(words1)]
words6 = [x[0] for x in words5]
s1 = SnowNLP(" ".join(words3))
print(s1.sentiments)
# 如果情感倾向是正向的，sentiment的结果会接近1。
# 如果情感倾向是负向的，结果会接近0。
