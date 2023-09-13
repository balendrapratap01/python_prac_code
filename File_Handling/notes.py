# open a file
# read a file
# close a file


# here we are trying to open a file thorugh various mode
file1 = open('abc.txt','r')
# now we are trying to read() a file

read_content = file1.read()
print(read_content)
file1.close()

