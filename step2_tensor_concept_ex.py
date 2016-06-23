#-*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

state1 = tf.Variable(0, name="counter")
init_op = tf.initialize_all_variables()

with tf.Session() as sess:
	print "sess.run(init_op): ", sess.run(init_op)
	print "sess.run(state1): ", sess.run(state1)
	
	print "state1.assign(2):", state1.assign(2)
	print "sess.run(state1): ", sess.run(state1)
	"""
	여기서 변수값이 2이 아니라 그전 변수값인 0이 나온 이유는 
	state1.assign(2) 자체는 tensor 를 생성하는 행위이고
	따라서 변수값 변경이 적용되도록 만드려면, 다음과 같이 작업해주어야 합니다.
	"""
	assign_op = state1.assign(2)
	print "sess.run(assign_op): ", sess.run(assign_op)
	print "sess.run(state1): ", sess.run(state1)