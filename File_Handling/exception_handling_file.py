# if an exception occurs when we are peforming some operations with the file,
# the code exists without closing the file. a safer way is try and finally

try:
    file1 = open('abc.txt','r')
    read_content = file1.read()
    print(read_content)

finally:
    # close the file
    file1.close()