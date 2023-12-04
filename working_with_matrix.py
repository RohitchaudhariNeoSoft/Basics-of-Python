## Importing Liabrary
import numpy as np

## Creating Matrix
arr1 = np.array([[1,2,3],
                 [4,5,6]])
print(arr1)

print("Data type of array: ",arr1.dtype)
print("Dimension of array: ",arr1.ndim)
print("Shape of array: ",arr1.shape)
print("size of array: ",arr1.size)

## Copying array
arr2 = arr1  # Shallow copy
arr3 = arr1.copy()  #Deep copy


## converting 2D array to 1D array
arr2 = arr1.flatten()
print("Flattened array : ",arr2)

## Converting 1D array to 2D using Reshape
arr3 = arr2.reshape(3,2)
print("Reshaping an array: ",arr3)


## Creating an matrix
m = np.matrix('1 2 3; 4 5 6; 7 8 9')
print("Matrix is :",m)

## Diagonal elements
print("Diagonal Elemnts : ", np.diagonal(m))

print("Minimum element from matrix : ", m.min())
print("Maximum element from matrix : ", m.max())

## Matrix Addition
m1 = np.matrix('1 2 3; 4 5 6; 7 8 9')
m2 = np.matrix('10 11 12; 13 14 15; 16 17 18')

addition = m1 + m2
print("Addition of two matrix is: ",addition)

## matrix Multiplication
dot_prod = np.dot(m1,m2)
print("Dot product of matrix is : ",dot_prod)

cross_prod = np.cross(m1,m2)
print("Cross product of matrix is : ",cross_prod)

## Finding Transpose of the matrix
trans = np.transpose(m1)
print("Transpose of the matrix m1 : ",trans)


