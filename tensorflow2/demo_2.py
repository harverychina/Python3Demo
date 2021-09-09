# coding:utf-8
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant(1.)
b = tf.constant(2.)
c = tf.constant(3.)
w = tf.constant(4.)

with tf.GradientTape() as tape:
    tape.watch([w])
    y = a * w ** 2 + b * w + c

[dy_dw] = tape.gradient(y, [w])
print(dy_dw)
