# for each try block there can be zero or more except blocks.
# multiple except block allow us to handle each exception

try:
    even_numbers = [2,4,6,8]
    print(even_numbers[5])   # here we are trying to print 5th index

except ZeroDivisionError:
    print("Denominator cannot be 0. ")
except IndexError:
    print("index out of found. ")


# hence ZeroDivisionError skipped and IndexError executed


