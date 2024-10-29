import numpy as np

arr = np.array([1, 2, 3, 4]) # 1-D Array

# Access element at index 2

print(arr[2])

# Access element on index 1 on 2nd row

two = np.array([[1,2,3],[4,5,6]]) 

print(two[1, 1])

three = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(three[1, 1, 2]) # access element on 2nd row, 2nd column, 3rd dimension