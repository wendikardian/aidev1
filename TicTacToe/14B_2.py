import numpy as np

a = np.array([1, 2, 3, 4, 5, ])
b = np.array([6, 7, 8, 9, 10])
c = np.add(a,b)
# print(c)
# print(a+b)

DualDimension = np.array([[1, 2, 3, 4, 5,], [6, 7, 8, 9, 10]])
print(DualDimension)
print(DualDimension.diagonal(3))
# print(DualDimension[0][2])