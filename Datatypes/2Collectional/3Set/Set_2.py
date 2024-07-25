# Set Functions and Methods

# functions
x = {10,20,30,40,50}

print(type(x)) # returns the datatype

print(id(x)) # returns the memory address of value

print(len(x)) # returns the length of value

print(min(x)) # returns the minimum val

print(max(x)) # returns the minimum val

print(sorted(x)) # order the values and returns into list

print(reversed(sorted(x))) # when using reversed fn o/p is in indirect address
# how can display the values for reversed fn ? using for loop

for i in reversed(sorted(x)):
    print(i,end=' ')




# Methods

x = {10,20,30,40,50}
print(x)

# add() ---> insert the new value
x.add(60)
print(x)

# remove() ---> removes the value
x.remove(60)
print(x)

#copy() -----> copy to another variable
y = x.copy()

print(y)


# union = returns all values(common values print only once)

a = {10,20,30,40}
b = {30,40,50,60}

print(a.union(b))

# Intersection = returns only common values

print(a.intersection(b))


# difference

a = {10,20,30,40}
b = {30,40,50,60}

print(a.difference(b)) # only prints different values of a
print(b.difference(a)) # only prints different values of b



# update = we can use for multiple values insertion into set

x = {10,20,30,40}

x.update({50,60,70,80})
print(x)


# clear --> removes all items/values  in the set

x = {10,20,30}
x.clear()
print(x)