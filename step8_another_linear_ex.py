import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

num_points = 1000
vectors_set = []
for i in xrange(num_points):
	x1 = np.random.normal(0.0, 0.55) # normal distribution (mean, sigma)
	y1 = x1*0.1 + 0.3 + np.random.normal(0.0, 0.03)
	vectors_set.append([x1, y1])

x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

theta = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
h = theta * x_data + b
loss = tf.reduce_mean(tf.square(h - y_data))
#alpha = 0.1
alpha = 0.5
#alpha = 0.9

optimizer = tf.train.GradientDescentOptimizer(alpha)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)
print "step theta b loss"
for step in xrange(8):
	sess.run(train)

	print step, sess.run(theta), sess.run(b), sess.run(loss)
	plt.plot(x_data, y_data, 'ro', label='Original data')
	plt.plot(x_data, sess.run(theta)*x_data+sess.run(b), 'y-', label='hyper function')
	plt.xlabel('x')
	plt.xlim(-2, 2)
	plt.ylabel('y')
	plt.ylim(0.1, 0.6)
	plt.legend()
	plt.show()