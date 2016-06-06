import tensorflow as tf
import numpy as np

x = [1,2,3]
# case 1 : '*' operation on python
prod1 = 2*x
print "prod1", prod1

# case 2 : '*' operation on np.array()
prod2 = 2*np.array([1,2,3])
print "prod2", prod2

# case 3 : '*' operation on tensorflow
prod3 = tf.constant(2)*x + tf.constant(5)
with tf.Session() as sess:
	print "prod3", sess.run(prod3)

