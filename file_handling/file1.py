# file reading function types ===> 2

# 1. open()
# 2. with

f = open(""
"/home/siva/Documents/python_june_8pm_to_9pm_batch/" \
"python_june_8pm_to_9pm_batch/file_handling/sample.txt""") # if mode is not mentioned by-default it will take as 'r'

print(f)

# read()
print(f.read())

f.close() # closes the file

# note : when ever using open() fn must be use the close() for closing the files


#2. with ----> no need to closing the file, with will automatically closes the file

with open(""
"/home/siva/Documents/python_june_8pm_to_9pm_batch/" \
"python_june_8pm_to_9pm_batch/file_handling/sample.txt""",mode='r') as f:
    data = f.read()
    print(data)
