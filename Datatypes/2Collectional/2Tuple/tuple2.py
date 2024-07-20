# tuple functions and methods


# functions

x = (10,20,30,40,50,60)
print(x)

print(type(x))

print(id(x)) # returns the address of tuple

print(min(x)) # minimum

print(max(x)) # maximum

x = (10,20,5,0)
print(sorted(x)) # aggange values in ascending order and returns in list




# Methods

x = (10,20,30,40,50)

# x.append(60) # not works with tuple

# x.insert(2,200) # not works with tuple

# x.pop()# not works with tuple

# x.pop(2) # not works with tuple

# x.remove(40)# not works with tuple

# x.extend((60,70))# not works with tuple

# y = x.copy()# not works with tuple

print(x)
print(x.index(40)) # returns the index of a value
print(x.count(40)) # returns the no. of occurences of a value

# x.clear()# not works with tuple
print(x)