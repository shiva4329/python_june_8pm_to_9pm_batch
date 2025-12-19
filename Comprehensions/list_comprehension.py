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