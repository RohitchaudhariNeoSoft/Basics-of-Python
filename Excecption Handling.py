def divide_numbers(a, b):
    try:
        result = a / b  # Attempt to perform the division
    # except Exception:               # Base Exception handling
    #     print("In Exception block")
    except ZeroDivisionError:            # specific exceptions
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Please provide valid numeric values.")
    finally:            #This block always executes
        print("This block always executes, regardless of whether an exception occurred.")

divide_numbers(10, 2) # Output: Division result: 5.0 \n This block always executes, regardless of whether an exception occurred.
print("*"*100)        
divide_numbers(10, 0) # Output: Error: Division by zero is not allowed. \n This block always executes, regardless of whether an exception occurred.
print("*"*100)     
divide_numbers("10", 2) # Output: Error: Please provide valid numeric values. \n This block always executes, regardless of whether an exception occurred.


## If we write Base Exception above the specific exception it will executes always on every exception.
## So there is no need of specific exception.
## If you want to execute the specific exception then you have to write specific exception above Base exception.