# filter with lamda function
x = range(1,21)
y = filter(lambda a: a%2 == 0, list(x))
print(list(y))