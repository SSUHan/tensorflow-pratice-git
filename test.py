import tensorflow as tf
ran = tf.Variable(tf.random_uniform([1], -1, 1))
#ran = tf.Variable(0, name="counter").assign(tf.random_uniform([1], -1, 1))
# var = tf.Variable(0.)
# rand = tf.random_uniform([1], -1, 1)
# assi = var.assign(rand)
init = tf.initialize_all_variables()
with tf.Session() as sess:
	sess.run(init)
	for i in xrange(2001):
		if i % 100 == 0:
			print i, sess.run(ran)