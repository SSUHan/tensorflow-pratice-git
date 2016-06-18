#-*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

t = tf.zeros([3,]) # 제로 매트릭스를 만드는 방법입니다.
with tf.Session() as sess:
    print sess.run(t)

# random_uniform : 균등분포에서 아무값을 뽑아내는 행위 : 랜덤값을 얻는 방법 
t1 = tf.random_uniform([1], -1, 1) # 인자값 : 매트릭스 크기, 시작 범위값, 끝 범위값
t2 = tf.random_uniform([2,2], 0, 1)
with tf.Session() as sess:
    print sess.run(t1)
    print sess.run(t2)

mat1 = tf.constant([[2,3]]) # [1, 2] matrix
mat2 = tf.constant([[2], [5]]) # [2, 1] matrix
product = tf.matmul(mat1, mat2) # 매트릭스 곱하기 연산
cons = tf.constant(1) # 벡터/ 매트릭스 가 아닌 일반상수일 경우에 타입을 확인하고 싶어서
 
with tf.Session() as sess:
    print mat1				# Tensor
    print mat1.eval()		# [[2 3]]
    print sess.run(mat1)	# [[2 3]]
    print sess.run(product)	# [[19]]
    print product			# Tensor
    print cons 				# Tensor