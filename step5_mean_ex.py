import tensorflow as tf
import numpy as np

np_array = np.array([[1,2], [3,4], [5,6]])

# mean operation using numpy
print "np.mean..."
print "rowwise mean :", np.mean(np_array,1) # 1 -> rowwise
print "columwise mean :", np.mean(np_array,0) # 0 -> columwise
print "total mean : ", np.mean(np_array) # none -> total

# mean operation using tensorflow
mean1 = tf.reduce_mean(np_array, 1)
mean2 = tf.reduce_mean(np_array, 0)
mean3 = tf.reduce_mean(np_array)

with tf.Session() as sess:
	print "tf.reduce_mean..."
	print "rowwise mean :", sess.run(mean1)
	print "columwise mean :", sess.run(mean2)
	print "total mean :", sess.run(mean3)

c = np.array([[1., 2], [3., 4], [5., 6]]) # float data
mean1 = tf.reduce_mean(c, 1)
mean2 = tf.reduce_mean(c, 0)
mean3 = tf.reduce_mean(c)

with tf.Session() as sess:
	print "float data operation.."
	print "rowwise mean :", sess.run(mean1)
	print "columwise mean :", sess.run(mean2)
	print "total mean :", sess.run(mean3)

c = [[1.,2], [3.,4], [5.,6]]
mean1 = tf.reduce_mean(c, 1)
mean2 = tf.reduce_mean(c, 0)
mean3 = tf.reduce_mean(c)

with tf.Session() as sess:
	print "no use np.array.."
	print "rowwise mean :", sess.run(mean1)
	print "columwise mean :", sess.run(mean2)
	print "total mean :", sess.run(mean3)
