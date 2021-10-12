# -*- coding: utf8
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant(3, tf.float32)
b = tf.constant(4, tf.float32)
c = tf.constant(5, tf.float32)
y = tf.add(a * b, c)
print(y)
