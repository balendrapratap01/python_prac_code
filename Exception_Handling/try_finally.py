# in python, the finally block is always executed no matter whether there is an exception or not

# the finally block is optional. and for each try: block, there can be only one finally block

try:
    num = 10
    den = 0
    
    result = num/den
    print(result)

except:
    print("Error: Denominator cannot be 0. ")

finally:
    print("This is finally bloc")