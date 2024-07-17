# mutable = iems changeable ----> we can chnage the items in the list


x = [10,20,30,40,50]
print(x)

# modify 20 to 200
x[1] = 200

print(x)

# modify 50 to 25
x[-1] = 25

print(x)

x = [10,20,30,40,50,60]
# x[2:4] = 500 # Error, bcoz of we cannot replace multiple values with single value while using index
print(x)


x = [10,20,30,40,50,60]
x[2:4] = 500,600 # replaces with new values bcoz we are passing multiple values at both like LHS = RHS
print(x)


# step size = it will display only particular values based on value mentioned in step size
#syntax : x[start:End:StepSize]


x = [10,20,30,40,50,60,70,80]

print(x[1::3])