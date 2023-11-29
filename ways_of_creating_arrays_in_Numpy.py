## Import Numpy Liabrary
import numpy as np

## By Using array

arr = np.array([1,2,3,4,5])
print(arr)
print(arr.dtype)  #Here the datatype of array is INT
print("*"*50)    

arr = np.array([1,2,3,4,5.0])
print(arr)
print(arr.dtype)    #Here the datatype of array is Float. It coverts the array implicitly.
print("*"*50) 



## By using linspace
arr = np.linspace(0,15,16)  #It will divide the range of 0 to 15 into 16 parts and datatype is float.
print(arr)
print("*"*50) 

arr = np.linspace(0,15,20)
print(arr)
print("*"*50) 


# By using Logspace
arr = np.logspace(0,15,10)  #Return numbers spaced evenly on a log scale.
print(arr)
print("*"*50) 

## By using arange
arr = np.arange(0,15,2)  #It will return values between 0 to 15 and stepsize is 2
print(arr)
print("*"*50)


## By using zeros
arr = np.zeros(5)  #It will return array of zeros and datatype is float.
print(arr)
print("*"*50)

## By using Ones
arr = np.ones(5)  #It will return array of ones and datatype is float.
print(arr)
print("*"*50)