#-*- coding: utf-8 -*-
import tensorflow as tf

matrix1 = tf.constant([[3,3]], name="Matrix1")
matrix2 = tf.constant([[2],[2]], name="Matrix2")
product = tf.matmul(matrix1, matrix2, name="Product")

# 그래프에 표현하고 싶은 데이터를 결정하고 summary에 추가
tf.histogram_summary("mat1", matrix1)
tf.histogram_summary("mat2", matrix2)
tf.histogram_summary("prod", product)

with tf.Session() as sess:
	# 그래프를 작성할 위치 지정
	writer = tf.train.SummaryWriter("/Users/myZZUNG/myworkspace/git-storage/tensorflow-git", sess.graph)
	# 위에서 추가한 summary들을 합병
	merged = tf.merge_all_summaries()
	# 작성한 그래프 저장
	summary,_=sess.run([merged, product], feed_dict={})
	writer.add_summary(summary)