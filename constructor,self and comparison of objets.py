class computer:
    
    def __init__(self):   ## Constructor
        self.name = "Rohit"
        self.age = 28
    
    def update(self):  ## To update the value
        self.age = 35

    def compare(self,other):   ## To compare 2 objects
        if c1.age == other.age:
            return True
        else:
            return False

c1 = computer()   ## Objects of an class
c2 = computer()

c1.name= "Rashi"
print(c1.name)
print(c2.name)

if c1.compare(c2):
    print("they are same")
else:
    print("they are different")