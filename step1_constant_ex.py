#-*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
 
a = tf.constant([1,2,3])
b = tf.constant([[10, 20, 30], [100, 200, 300]])
c = tf.add(a,b)
 
with tf.Session() as sess:
    print sess.run(c)

# 만약 tf.Session 을 열고, run 을 하지 않는다면?

print c