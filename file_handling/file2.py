# write operation = mode = 'w' --> creates the files if not exists

# creat the file and insert the data

with open('sample2.txt',mode='w') as f:
    data = f.write('Im python')

with open('sample2.txt',mode='w') as f:
    data = f.write('welcome to python')

#Note : operatios of 'w' mode

# 1. creates the files if not exists
# 2. inserts the data

# dis-advanatages:

# overwrites the old data
# read() fn does not support



with open('sample2.txt',mode='w+') as f:
    f.write('welcome to python')
    f.seek(0) # moves the cursor to begining and read the data
    print(f.read())

# print(data)

# Note : when ever using read fn in w+ mode use seek() fn for moving the cursor to read the data from req position
#           else returns empty data bcoz cursor will be in last position so no data from the last


with open('sample2.txt',mode='w') as f:
    f.write('welcome to python')
    # f.seek(0) # moves the cursor to begining and read the data
    # print(f.read())

with open('sample2.txt',mode='r') as f:
    print(f.read())