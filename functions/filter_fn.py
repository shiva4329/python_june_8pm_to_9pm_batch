#filter ---> it returns only True value
# syntax : filter(function, iterable)

# generate a list with even numbers from 1 to 20 using filter fn
def even(a):
    return a % 2 == 0   

x = range(1,21)
y = filter(even, list(x))
print(y) # return the address of filter object 
print(list(y)) # to print the values we need to convert it into list

# map vs filter
# map ---> it applies the function to all the values in the iterable and returns all the values
# filter ---> it applies the function to all the values in the iterable and returns only True values