# functions

x = {'x':10,'y':20,'z':10,'a':20}

print(x)

print(len(x))

print(id(x))

print(sorted(x))

print(type(x))


# methods 

x = {'x':10,'y':20,'z':10,'a':20}

print(x)

# keys() --> returns keys

print(x.keys())

# values() --> returns only values

print(x.values())

# items() -- prints each item seperatly in tuple

print(x.items())

# get() --- returns key value

print(x.get('z'))

# pop() -- removes an item in the dict
x.pop('a')
print(x)

# popitem() -- removes last item in the dict
x.popitem() 
print(x)


# setdefault -- if we are not passing particular key when using default method it sets the deffault value to that particular key
x = {'y':200,'x':10}
x.setdefault('x',1000)
print(x)

# clear --> removes all item in the dict
x.clear()
print(x)