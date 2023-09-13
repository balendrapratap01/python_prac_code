# python built in exceptions
# we can view all the built in exceptions using the built-in local() function

# print(dir(locals()['__builtins__']))

# python try and except bloc

try:
    num = 10
    deno = 0
    
    result = num/deno
    print(result)
except:
    print("Error: Denominator cannot be 0. ")
