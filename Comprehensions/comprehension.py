# comprehensions == can create list in single line

# list comprehension

# create list with 1 to 10 numbs

x = []

for i in range(1,10):
    x.append(i)

print(x)

# using comprehension

x = [i for i in range(1,10)]
print(x)

# how to create list with even numbers till 20
x = []

for i in range(1,20):
    if i % 2 == 0:
        x.append(i)

print(x)

x = [i for i in range(1,20) if i % 2 == 0]
print(x)


# tuple comprehension ---> it generates indirect addressable object so we need to use tuple() 
# to convert it into tuple

x = (i for i in range(1,10))
print(tuple(x))


# set comprehension --->
x = {i for i in range(1,10)}
print(x)

# dictionary comprehension ---> key:value pair
x = {i:f"item{i}" for i in range(1,10)}
print(x)

# create list of even values from 1 to 50 using list comprehension
x = [i for i in range(1,51) if i % 2 == 0]
print(x)

# create a dictionary with numbs from 1 to 10 as key and their squares as values using dictionary comprehension
x = {i:i**2 for i in range(1,11)}
print(x)
