import tensorflow as tf

matrix1 = tf.constant([[3,3]], name="Matrix1")
matrix2 = tf.constant([[2],[2]], name="Matrix2")
product = tf.matmul(matrix1, matrix2, name="Product")

tf.histogram_summary("mat1", matrix1)
tf.histogram_summary("mat2", matrix2)
tf.histogram_summary("prod", product)

with tf.Session() as sess:
	writer = tf.train.SummaryWriter("/Users/myZZUNG/myworkspace/git-storage/tensorflow-git", sess.graph)
	merged = tf.merge_all_summaries()
	summary,_=sess.run([merged, product], feed_dict={})
	writer.add_summary(summary)