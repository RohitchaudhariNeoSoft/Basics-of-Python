'''Decorator is a tool in Python that allows you to add functionality to functions 
without modifying their original code. They are essentially functions that take another 
function as an argument and return a new function. The new function, often referred to as 
the decorated function, retains the original function's functionality while also incorporating
the additional behavior introduced by the decorator.'''

## Decorator function to show how decorator works
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

## Decorator function calling
@my_decorator
def greet():
    print("Hello, world!")

# Calling the decorated function
greet()


'''Here's a breakdown of what's happening:

1.The my_decorator function takes another function (func) as its argument.
2.It defines a new function (wrapper) that adds behavior before and after calling func.
3.Inside wrapper, it calls the original function (func).
4.The decorator returns the wrapper function.

When you decorate the greet function with @my_decorator, it is equivalent to:
greet = my_decorator(greet)'''