'''Class:
A class is a blueprint or template for creating objects. 
It defines a set of attributes and methods that the objects of the class will have. 
Think of a class as a user-defined data type.

Objects:
An object is an instance of a class. 
It is a concrete entity based on the class, with specific values assigned to its attributes. 
Objects represent real-world entities and can perform actions through their methods.

Methods:
Methods are functions defined within a class. 
They represent the behavior of the class and are called on objects of that class. 
Methods can operate on the data within the class (attributes) and can perform various actions.'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

# Creating an object (instance) of the Dog class
my_dog = Dog(name="Buddy", age=3)

# Accessing attributes
print(my_dog.name)  # Output: Buddy

# Calling a method
my_dog.bark()  # Output: Woof!


# Creating two objects of the Dog class
dog1 = Dog(name="Charlie", age=2)
dog2 = Dog(name="Max", age=5)

# Accessing attributes
print(dog1.name)  # Output: Charlie
print(dog2.age)   # Output: 5

# Calling methods
dog1.bark()  # Output: Woof!
dog2.bark()  # Output: Woof!


'''In summary, a class defines a blueprint, an object is an instance of that blueprint, 
methods define the behavior of the objects, and self refers to the instance on which a 
method is called.'''