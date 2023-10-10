from random import random
import numpy as np

# Initialization the numpy array 1d, 2d, or 3d

# 1D array
arrayValue = np.array([1,2,3,4])
print(arrayValue)

#2D array
coordinates = np.array([[1.0 ,2.0],[5.0 ,3.0]])
print(coordinates)


# To find the dimension of the np.array 
print(arrayValue.ndim)
print(coordinates.ndim)

# To find the shape dimension of the np.array
print(coordinates.shape)

# To find data type of numpy array
print(coordinates.dtype)

# Get size of numpy array
print(coordinates.itemsize)


# Get total size
print(coordinates.size * coordinates.itemsize)
# or 
print(coordinates.nbytes)


data = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(data.shape)
print(data)

# Access the element of  the numpy array
print(data[0,5])
print(data[0,-1])


# Get a specific row
print(data[0])
print(data[0, :])


# Get a specific column
print(data[:, 2])


# Get a little bit a data with a specific range
print(data[0, 1:6])
# Add a step in there
print(data[0, 1:6: 2])

# Change an element from numpy
data[1, 6] = 99
print(data)


# Change a specific column
data[:, 3] = 101

# Or
data[:,4] = [88, 44]
print(data)

# 3D Example
data3D = np.array([[[10, 20], [30, 40]], [[50,60], [70,80]]])
print(data3D)

# Get element data using work outside in
print(data3D[1,1,:])
# NOTESS
# should insert data to a specific size
# 2,2 -> 2,2 cannot with 2,1

# Change 3D data
data3D[0,1, :] = [99,100]
print(data3D)

# It will caused an error
# data3D[0,0, :] = [200, 300, 999]


# Initialization difference types of numpy arrays
# All 0s Matrix
zeros1 = np.zeros(5)
zeros2 = np.zeros((2,4))
zeros3 = np.zeros((3,4,5))

# print(zeros3)

# All 1s matrix

# Search data type on the numpy
dataOnes = np.ones((5,2,3), dtype='int32')
print(dataOnes)

data3D = np.array([[[10, 20], [30, 40]], [[50,60], [70,80]]])

# Copy a data from numpy
# Copy data3D variable to copyData3D and fill it with number 4
copyData3d = np.full_like(data3D, 4)
print(copyData3d)


# Create a random decimal numbers
randomDecimals = np.random.rand(4, 2)
randomDecimals2 = np.random.rand(4, 2,3)
print(randomDecimals)
print(randomDecimals2)


# Create a random integer value
randomInteger1 = np.random.randint(4, 7, size=(3,3))
# 7 means it the max value and 4 is minimum value
print(randomInteger1)


# Create an identity matriks
identityMatrix = np.identity(3)
print(identityMatrix)

# Create an repeatable numpy array
# First create 2D np array 
arr1 = np.array([[1,2,3]])
repeatArr1 = np.repeat(arr1, 3, axis = 0)
print(repeatArr1)


# Challenge to create a matrix with full of number 1

# Step 1. create an array with full of number 1 with matrix 5 x 5
output = np.ones((5,5))
print(output)

# Step 2. create an array with zeros with matrix 3 x 3
zerosArray = np.zeros((3,3))
print(zerosArray)

# Step 3. chang value from the middle matrix of zeros array with another number example 5
zerosArray[1,1] = 5
print(zerosArray)

# Step 4. Change the output with np.ones to zeros array
# output[1:4, 1:4] = zerosArray
# or
output[1:-1, 1:-1] = zerosArray

# -1 means is the last element of the array

print(output)


# BE CAREFUL WHEN COPYING AN ARRAYS
first = np.array([1,2,3])
second = first
# second[0] = 100

# When second is change, it also change the first ... so the first array is changing even tho the value that means to be changed is the array second
print(second)
print(first)
# Two above have the same result

# To prevent that we can use copy() method

second = first.copy()
second[0] = 100
print(second)
print(first)


# The Mathematics of NUMPY ----------------------------------------------------------------
first = np.array([1,2,3,4,5,6,7])
first += 2;
first *= 2;
# So other operator did the same thing
print(first)

second = np.array([-1,-2,-3,-4,-5,-6,-7])
first += second;
print(first)

# Create a power of 2 of each arrays
third = np.array([10,11,12,13,14])
third **=2;
print(third)

# Take the sin of the value array
print(np.sin(third))


# ------------ LINEAR ALGEBRA OPERATION ----------

a = np.ones((2,3)) 
print(a)
b = np.full((3,2), 2)
print(b)

# The multiple operation on matrix
print(np.matmul(a,b))

# Count determinant values from identity matrix

c= np.identity(3)
print(np.linalg.det(c))


# Statistics on numpy

stats = np.array([[1,2,3],[4,5,6]])
print(stats)
print(np.min(stats))
print(np.min(stats, axis = 1))
print(np.max(stats))

# Reorganizing arrays

# Chapter 1 -> Reshape

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before.shape)
after = before.reshape((1,8))
after = before.reshape((8,1))
after = before.reshape((4,2))
after = before.reshape((2,2, 2))
print(after)

# Chapter 2 -> Vertically Stacking vectors
vector1 = np.array([1,2,3,4])
vector2 = np.array([5,6,7,8])
vector3 = np.vstack([vector1, vector2, vector2, vector1])
print(vector3)

# Chapter 3 -> Horizontal Stack
horizontal1 = np.ones((2,4))
horizontal2 = np.full((2,2), 2)

horizontal3 = np.hstack((horizontal1, horizontal2))
print(horizontal3)


# Get data from file
dataNilai = np.genfromtxt('dataNilai.txt', delimiter=',')

# Convert into integer
dataNilai = dataNilai.astype('int32')
print(dataNilai)


# Advance indexing 
# Boolean masking

# filter data that the value > 70
# Will return the boolean is the data is greater that 70 or not
print(dataNilai > 70)

# Print the index that only greater than > 70
print(dataNilai[dataNilai > 70])

# Find the data from each row is there data greater that 70
print(np.any(dataNilai > 70, axis = 0))

# every column is must more > 70 (harus semua)
print(np.all(dataNilai > 70, axis = 0))




# Create empty and full numpy array
# emptyArray = np.empty([3,4], dtype=int)
# filledArray = np.full([3,3], 55, dtype=int)
# print(emptyArray)
# print(filledArray) 