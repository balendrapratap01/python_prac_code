# in some situations, we might want to run a certain block of code if the block inside
# try: runs without any errors

# for this case, we can use th eoptional else: keyword with the try: statement

# Programm to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2  == 0
except:
    print("Not an even numbre! ")
else:
    reciprocal = 1/num
    print(reciprocal)