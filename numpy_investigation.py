# numpy_investigation.py

import numpy as np

lst = [1, 2, 3, 4, 5]
print (lst)


arr = np.array([1, 2, 3, 4, 5])
print (arr)

# cration functions
zeros = np.zeros((4,3))
print (zeros)

ones = np.ones((4,3))
print (ones)

# aside - revisit the range
r = range(5)

for i in range(1, 10, 2):
    print (i)

# 
sequence = np.arange(0, 10, 2)
print (sequence)

# numpy really shines with more than 1 dimension
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print (arr)

arr = arr.reshape((3, 4))

print (arr)

# we can use the slice operators

print (arr[1:3, 1:3])


print (arr[1:, 1:])

# extract a full column

print (arr[:, 1])


# multiplication
print (arr * 10)


# extra random number features
rarray = np.random.randint(1, 100, (5, 5))
print (rarray)

















