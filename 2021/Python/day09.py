import numpy as np
from scipy.signal import convolve2d

arr = np.array([[1, 2, 3], [4, 5, 6]])

c = np.ones(shape=(3, 3), dtype=np.int8)
c[1, 1] = 0
c[0, 0] = 0
c[2, 0] = 0
c[2, 2] = 0
c[0, 2] = 0

print(c)
