import numpy as np #Mengimport library Numpy agar bisa digunakan
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
print(a) # Menampilkan output dari Numpy array yang sudah dibuat
print(b) # Menampilkan output dari Numpy array yang sudah dibuat

Array2D = np.array([[1,2,3,4,5], 
                    [6,7,8,9,10], 
                    [11,12,13,14,15]])

print(Array2D[0, 2])

data = np.array([[1,2,3,4], 
                 [5,6,7,8]])

print(data[:, 2])

print(data[1, :])

print(data[:, 1:3])


print(data[1, 1:4])


empty = np.zeros((4,4), dtype="int")

empty[0, 1:4] = [1,55,3]

print(empty)