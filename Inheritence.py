class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):  # Single-level inheritance
    def bark(self):
        print("Woof!")

class Mammal(Animal):  # Base class for multi-level inheritance
    def give_birth(self):
        print("Giving birth...")

class Bat(Mammal, Dog):  # Multi-level and multiple inheritance
    def fly(self):
        print("Flying...")

# Create instances
dog = Dog()
mammal = Mammal()
bat = Bat()

# Single-level inheritance
print("Single level Inheritence :")
dog.eat()  
dog.bark()  
print("*"*50)
# Multi-level inheritance
print("Multiplevel inheritence output: ")
mammal.eat()  
mammal.give_birth()  
print("*"*50)
# Multiple inheritance
print("Multiple Inheritence output: ")
bat.eat()  
bat.give_birth()  
bat.bark() 
bat.fly()  
