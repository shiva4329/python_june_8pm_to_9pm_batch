# append('a') ---> appends the data into files

# append the data into existing file

with open('sample2.txt',mode='a') as f:
    f.write("12345678910")
    # print(f.read())


with open('sample2.txt',mode='r') as f:
    print(f.read())


# Note : append the data into the from from the last position of cursor

# how to append the data into file in next line
# append the data into existing file

with open('sample2.txt',mode='a') as f:
    f.write("\nABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # print(f.read())