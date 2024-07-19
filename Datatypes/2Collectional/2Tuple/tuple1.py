#




x = () # empty tuple
print(x,type(x))


x = 10,20,30 # note : by default is we are passing multiple values with-out any braces it will treats as a tuple
print(x,type(x))

x = (10,20,30)
print(x,type(x))


# homogeneous ---> same type of values

x = (10,20,30,40)
print(x)

y = ('a','b','c')
print(y)


# heterogeneous ---> different type of values

x = (10,'hello',12.01,False,10+2j)
print(x,type(x))

# duplictaes

x = (10,20,10,0,20)
print(x,type(x))


# index
x = (10,20,30,40)
print(x[1:3])

x = (10,20,30,40)
print(x[-3:-1])




#immutable

x = (10,20,30,40)

# x[2] = 300 # error : tuple dosent allow value modification
print(x,type(x))


y = [10,20,30,40]

y[2] = 300
print(y,type(y))