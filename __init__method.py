""" The __init__ method, also known as the constructor, is a special method in Python 
classes that automatically runs whenever a new instance of the class is created. 
Its primary purpose is to initialize the object's attributes and perform any necessary setup
 before it's used."""

class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

dog1 = Dog("Max", "Golden Retriever")
dog2 = Dog("Luna", "Labrador Retriever")

print(f"{dog1.name} is a {dog1.breed}.")  # Output: Max is a Golden Retriever.
print(f"{dog2.name} is a {dog2.breed}.")  # Output: Luna is a Labrador Retriever.


"""
1.The __init__ method in the Dog class takes two arguments: name and breed.
2.Inside the method, the self keyword refers to the newly created object.
3.We use self.name = name and self.breed = breed to assign the passed values 
to the object's attributes.
4.The subsequent object creations (dog1 and dog2) provide values for name and breed,
which are then assigned to their respective attributes."""