
""" 
There are 3 methods in th Python:

1. Instance method : 
        -- Self is given as an parameter.
        -- They access and modify both object and class attributes.

2. Class Methods :
        -- They access and modify class attributes but not object attributes.
        -- Defined using the @classmethod decorator and the "cls" parameter:

3. Static Methods :
        -- They neither access nor modify class or object attributes.
        -- Defined using the @staticmethod decorator.
"""

class student:

    school = "VITA"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):   ##instance method
        return (self.m1 + self.m2 + self.m3)/3
    
    @classmethod
    def getschool(cls):   ##Class Method
        return cls.school

    @staticmethod
    def info():    ##Static Method
        return "This is student class in abc module"
    
s1 = student(24,34,64)
s2 = student(2,10,15)

print(s1.avg())
print(student.getschool())
print(student.info())




# Accessor methods -- Used only to fetch values and does not change the values -- getter method
# Mutator methods -- Used only to modify the values and can change the values -- setter methods


## Instance method -- self is used
## Class Method -- cls is used,.. --To define class method @ClassMethod is used -- 
## Static method -- -- to define static method @Staticmethod is used
