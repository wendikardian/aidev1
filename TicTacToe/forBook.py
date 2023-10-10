import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([6.0 ,7.0 ,8.4 ,9.5 ,10.8])    
print(a)
print(b)


# c = np.array([1,2,3,"empat",5])
# print(c)


Array2D = np.array([[1,2,3,4,5], 
[6,7,8,9,10],
[11,12,13,14,15]])

# print(Array2D)

a = np.array([1,2,3,4,5])
b = np.array([6.0, 7.0, 8.4, 9.5, 10.8])
Array2D = np.array([[1,2,3,4,5], 
[6,7,8,9,10],
[11,12,13,14,15]])
# print("Tipe data numpy array a : " + str(a.dtype))
# print("Tipe data numpy array B : " + str(b.dtype))
# print("Ukuran numpy array A : " + str(a.shape))
# print("Ukuran numpy array 2D : " + str(Array2D.shape))
# print("Dimensi numpy array B : " + str(a.ndim))
# print("Dimensi numpy array 2D : " + str(Array2D.ndim))



array3D = np.array([[[1,2,3], [4,5,6]],
[[7,8,9], [10,11,12]],
[[13,14,15], [16,17,18]]])


before = np.array([[1,2,3,4],[5,6,7,8]])
# print(before)
# Tambahkan code dibawah ini
# after = before.reshape((1,8))
# print(after)
# after = before.reshape((8,1))
# print(after)
# after = before.reshape((4,2))
# print(after)
# after = before.reshape((2,2, 2))
# after = before.reshape((3,3))
# print(after)


# before = np.array([[1,2,3,4],[5,6,7,8]])
# print(before)

data = np.array([[1,2,3,4], [5,6,7,8]])
# Tambahkan code di bawah ini
# print(data.diagonal(2))
# print(data[:, 1:3])
# print(data[1, 1:4])
# print(data.diagonal(-1))

empty = np.zeros((4,4), dtype="int")
empty[0, 1:4] = [1,55,3]
empty[-1, 0] = 7
empty[1:3, 1] = [9,5]
# print(empty)


c = np.array([3,6,9,12])
d = np.array([2,4,6,8])
# print(np.add(c,d))
# print(np.subtract(c,d))
# print(np.multiply(c,d))
# print(np.divide(c,d))

# print(c.sum(), d.sum())
# print(c.min(), d.min())
# print(c.max(), d.max())