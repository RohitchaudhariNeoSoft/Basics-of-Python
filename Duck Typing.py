def print_shape(obj):
    obj.print_details()

class Square:
    def print_details(self):
        print("Square")

class Circle:
    def print_details(self):
        print("Circle")

square = Square()
circle = Circle()

print_shape(square)  # Output: Square
print_shape(circle)  #output : Circle

##This example demonstrates how print_shape can work with any object that has a 
# print_details method, regardless of its specific type.
