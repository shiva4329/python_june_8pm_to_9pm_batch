# List

# list can be defined using [] braces
# list is a mutable(changeable)
# list allows duplicate values
# list allows homogeneous and heterogeneous values
# list follows index
# list function = list()


# defining list ---> using []

x = [] # retunrs list type
print(x,type(x))


x = [10,20,30]
print(x,type(x))

# duplicates

x = [10,10,20,20,30] # allows duplicates
print(x,type(x))


# homogonenous = same type of values
x = [10,20,30]
print(x,type(x))


# heterogenenous = diff type of values
x = [10,12.1,'a',True,10+2j]
print(x,type(x))



# index ---> 2types -> forward,backward
#       forward --> left to Right(----->) ----> starts with 0
#       backward --> Right to left(<----) ----> starts with -1


x = [10,20,30,40]
print(len(x))

print(x[2])
print(x[-2])


print(x[0:3])
print(x[-3:-1])

# combination of both +ve and -ve index
print(x[-3:3])


print(x[0:-1])
print(x[1:-2])
print(x[1:-3])

print(x[2:-1])

print(x[-1:1]) # returns empty list bcpz of printing from right to left that is not possible with print fn



x = [10,20,30,40,50]

print(x[-1:-3]) # returns empty bocz the printing direction is backward(but it shouls be forward direction only)

print(x[3:0]) # upper bound should be greater than else return empty


# note : upper bound should be greater tha lower bound
# note : print always prints in left to right directs
# note : if we are using same type index upper bound should be greater than
# note : if we are using combination index(both +ve and -ve) this should consider direction(forward direction)

