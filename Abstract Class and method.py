
from abc import ABC, abstractmethod 


class Polygon(ABC): 

	@abstractmethod
	def noofsides(self): 
		pass


class Triangle(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 3 sides") 


class Pentagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 5 sides") 


class Hexagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 6 sides") 


class Quadrilateral(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 4 sides") 


# Driver code 
R = Triangle() 
R.noofsides() 

K = Quadrilateral() 
K.noofsides() 

R = Pentagon() 
R.noofsides() 

K = Hexagon() 
K.noofsides() 


"""This code defines an abstract base class called “Polygon” using the ABC (Abstract Base Class) 
module in Python. The “Polygon” class has an abstract method called “noofsides” that needs to be 
implemented by its subclasses. There are four subclasses of “Polygon” defined: “Triangle,” 
“Pentagon,” “Hexagon,” and “Quadrilateral.” Each of these subclasses overrides the “noofsides” 
method and provides its own implementation by printing the number of sides it has.
In the driver code, instances of each subclass are created, and the “noofsides” method is called on 
each instance to display the number of sides specific to that shape."""


print("#"*100)
print("Concrete method in abstract base class code output:")
### Concrete methods in abstract base class

# Python program invoking a 
# method using super() 

from abc import ABC, abstractmethod 

class R(ABC): 
	def rk(self): 
		print("Abstract Base Class") 

class K(R): 
	def rk(self): 
		super().rk() 
		print("subclass ") 

# Driver code 
r = K() 
r.rk() 
