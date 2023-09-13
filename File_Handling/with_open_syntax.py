# since every time we have to close the file manullay so 
# we can use with open syntax , it will automatically close the file

with open('abc.txt','r') as file1:
    read_content = file1.read()
    print(read_content)