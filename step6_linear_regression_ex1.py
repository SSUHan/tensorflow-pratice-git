import tensorflow as tf
import numpy as np

x_data = [1, 2, 3]
y_data = [4, 7, 8]

# calculate cost loss = 1/m * sum{(h-y)^2}
# if hyper function would be h = 2*x + 1
h = tf.constant(2)*x_data + tf.constant(1)
diff = h - y_data
loss = tf.reduce_mean(tf.square(diff))

with tf.Session() as sess:
	print "h :", sess.run(h)
	print "y :", y_data
	print "diff :", sess.run(diff)
	print "loss :", sess.run(loss)