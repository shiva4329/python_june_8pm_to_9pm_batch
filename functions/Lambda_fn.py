# ananoumus fun = lambda fn

# syntax :
# lambda params : expression


x = lambda a : a+10

print(x(10))
print(x) # return the address


x = lambda a,b : a+b

print(x(100,200))


# crea a list with even numbers using lambda function

x = range(20)

y = filter(lambda a: a%2 == 0, list(x))

print(list(y))

# filter fn = it returns only True value

# filter,map,reduse