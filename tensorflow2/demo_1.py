# coding:utf-8
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant(2.)
b = tf.constant(4.)
print('a+b=', a + b)
