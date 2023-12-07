class student:          ##Outer Class

    def __init__ (self,name,rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.rollNo)

    class laptop:           ## Inner Class

        def __init__(self):
            self.brand = "Hp"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu, self.ram)



s1 = student("rohit", 22)
s2 = student("Ankur",20)
s3 = student.laptop()  ## creating object of inner class


print(s1.name, s1.rollNo)
print(s2.name, s2.rollNo)

s1.show()     ## Calling method from student
s3.show()     ## Calling method from inner class i.e, Laptop
   