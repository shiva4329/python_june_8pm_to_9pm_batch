# map ---> mapps the vavles to a function and returns the values after applying the function
# syntax : map(function, iterable)

# generate a list with squares of numbs from 1 to 10 using map fn

def square(a):
    return a**2 

x = range(1,11)
y = map(square, list(x))
print(y) # return the address of map object
print(list(y)) # to print the values we need to convert it into list

# with out map fn
def square(a):
    return a**2

x = range(1,11)
y = []
for i in x: 
    y.append(square(i))
print(y)


# generate a list with even of numbs from 1 to 10 using map fn ?