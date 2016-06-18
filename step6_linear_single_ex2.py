import tensorflow as tf
import numpy as np

# A single variable simple linear regression
x_data = [1,2,3]
y_data = [3,5,7]

theta = tf.Variable(tf.random_uniform([1], -1, 1))
b = tf.Variable(tf.random_uniform([1], -1, 1))
h = theta*x_data+b
diff = h-y_data
loss = tf.reduce_mean(tf.square(diff))

alpha = tf.Variable(0.1)

optimizer = tf.train.GradientDescentOptimizer(alpha)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

with tf.Session() as sess:
	sess.run(init)
	print "[i] [loss] [theta] [b]"
	
	for i in xrange(20):
		sess.run(train)
		print i, sess.run(loss), sess.run(theta), sess.run(b)