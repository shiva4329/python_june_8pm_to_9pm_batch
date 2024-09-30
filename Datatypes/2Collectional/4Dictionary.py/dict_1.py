#

# dictionary defining

x = {'x':10,'y':20}
print(x,type(x))

print(x['x'])
print(x['y'])

# x = {1:10,2:20,3:30}
# print(x,type(x))


# mutable ---> items can be changebale

x['x'] = 100

print(x)

# duplicate values

x = {'x':10,'y':20,'z':10,'a':20}

print(x)

# duplicate keys

x = {'x':10,'y':20,'x':100,'a':20}

print(x)

# note : if we are passing different values to same key it will take only latest value


# heterogeneous
x = {'x':10,'name':'miller','age':25.6,'status':True}

# print(x)

# print(x['x'])

# index = dict dosent follow index