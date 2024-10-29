import numpy as np

# 0-dim array
zero = np.array(100)

# 1-dim array
one = np.array([1,2,3])

# 2-dim array
two = np.array([[1,2,3],[4,5,6]]) 

# 3-dim array
three = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# Print number of dimensions of array using ndim attribute
print(zero.ndim)
print(one.ndim)
print(two.ndim)
print(three.ndim)   