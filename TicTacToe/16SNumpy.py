# data = [1, "Wendi", True, 1.0, 1+1j]
# print(data)


import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

two_dimentional = np.array(
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])

array3D = np.array(
    [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
        [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]]
)

# print(two_dimentional)
# print(two_dimentional[1][3])

print(array3D[1][0][1:3])
