import tensorflow as tf
import numpy as np

xy = np.loadtxt("train", unpack=True, dtype='float32')

x = xy[0:-1]
y = xy[-1]

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
theta = tf.Variable(tf.random_uniform([1, len(x)], -1, 1)) # [1,3] random matrix

h = tf.matmul(theta, X) # [1, 6]
hypothesis = tf.sigmoid(h) # [1, 6]

cost = -tf.reduce_mean(Y*tf.log(hypothesis) + (1-Y)*tf.log(1-hypothesis))

alpha = tf.Variable(0.1)

optimizer = tf.train.GradientDescentOptimizer(alpha)
train = optimizer.minimize(cost)

init = tf.initialize_all_variables()

with tf.Session() as sess:
	sess.run(init)
	print sess.run(cost, feed_dict={X:x, Y:y})

	for i in xrange(20):
		print i, sess.run(train, feed_dict={X:x, Y:y}), sess.run(cost, feed_dict={X:x, Y:y}), sess.run(theta)

