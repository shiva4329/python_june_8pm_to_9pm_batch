# reduce ---> to reduce a list to a single value
# syntax : reduce(function, iterable)
from functools import reduce
# generate a list with sum of numbs from 1 to 10 using reduce fn

def sum(a,b): #a =1, b=2  3 4 5 6 7 8 9 10
    return a+b
x = range(1,11)
y = reduce(sum, list(x))
print(y) # to print the values we need to convert it into list

# generate a list with product of numbs from 1 to 5 using reduce fn 

def product(a,b): # a=1, b=2  2 3 4 5
    return a*b

x = range(1,6)
y = reduce(product, list(x))
print(y)