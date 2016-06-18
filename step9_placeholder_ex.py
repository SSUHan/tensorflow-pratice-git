import tensorflow as tf

# placeholder example #1
x = tf.placeholder("float", [2, 3])
y = tf.ones([2, 3], "float")
result = tf.add(x, y)

with tf.Session() as sess:
	print "placeholder example #1"
	print sess.run(result, feed_dict={x:[[1,2,3], [4, 5,6]]})

# placeholder example #2

x = tf.placeholder("float", [2,3])
y = tf.placeholder("float", [2,3])
result = tf.add(x,y)

with tf.Session() as sess:
	print "placeholder example #2"
	print sess.run(result, feed_dict={x:[[1,2,3], [4,5,6]], y:[[3,4,5], [6,7,8]]})
