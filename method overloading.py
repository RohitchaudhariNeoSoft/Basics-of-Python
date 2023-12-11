
## method Overloading
from multipledispatch import dispatch

@dispatch(int, int)
def product(first, second):
	result = first*second
	print(result)

@dispatch(int, int, int)
def product(first, second, third):
	result = first * second * third
	print(result)

@dispatch(float, float, float)
def product(first, second, third):
	result = first * second * third
	print(result)

product(2, 3) # this will give output of 6

product(2, 3, 2) # this will give output of 12

product(2.2, 3.4, 2.3) # this will give output of 17.985999999999997




