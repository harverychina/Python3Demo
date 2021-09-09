# coding:utf-8
import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

data = []
for i in range(100):
    x = np.random.uniform(-10, 10.)
    eps = np.random.normal(0., 0.01)
    y = 1.477 * x + 0.089 + eps
    data.append([x, y])

data = np.array(data)
print(data)
