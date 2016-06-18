import tensorflow as tf
import numpy as np

xy = np.loadtxt("train", unpack=True, dtype='float32')
x = xy[0:-1]
y = xy[-1]

print 'xy: \n', xy
print 'x : \n', x
print 'y : \n', y
print 'type(x) :', type(x)
print 'x shape :', x.shape
print 'length of x:', len(x)
print 'x size:', x.size

print 'y shape:', y.shape
print 'y size:', y.size 