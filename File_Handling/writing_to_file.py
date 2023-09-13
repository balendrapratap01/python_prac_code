# there are two things we need to remember while writing to a file

# 1. if we try to open a file that doesn't exist, a new file is created

# 2. if a file already exists, its content is erased, and new content is added to the file


with open('abc2.txt','w') as file1:
    file1.write('Welcome to 2023 Balendra!.')
