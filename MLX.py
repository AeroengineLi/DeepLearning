import mlx.core as mx
import numpy as np

a = mx.array([[1.0, 2, 3, 4],[1,1,1,1]])
print(a)
print(a.shape)
b = np.array([[1,2,3,4],[1,1,1,1]])
print(b)
print(b.shape)
c = np.array(a)
print(c)