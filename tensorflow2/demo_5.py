# -*- coding: utf8
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
a = 3
b = 4
c = 5
y = a * b + c
print(y)
y = tf.add(a * b, c)
print(y)
