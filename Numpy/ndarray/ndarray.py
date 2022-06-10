'''Created by Al amin Kawsar 10th Jun,2022'''
'''Source from https://numpy.org/doc/stable/reference/arrays.ndarray.html'''
import numpy as np
x = np.array([[1,2,3],[4,5,6]],np.int8)
print(x)

print(x.shape)

print(x.dtype)

'''Slicing'''
y = x[:,1]
print(y)

d = np.ndarray(shape=(2,2),dtype=int)
print(d)

zeros = np.zeros(shape=(2,2),dtype=int)
print(zeros)