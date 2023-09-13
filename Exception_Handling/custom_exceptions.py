# In Python, we can define customs exceptions by creating a new class that is derived from the 
# built-in Exception class

# here's the syntax to define custom exceptions,

# class CustomError(Exception):
#     pass

# try:
#     num = 10
#     deno = 0

#     result = num/deno
#     print(result)
# except CustomError:
#     # self make CustomError
#     print("Check kar phir se........")

# PythonUser-Defined Exceptions example

class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
except InvalidAgeException:
    print("Exception occured: invalid age")