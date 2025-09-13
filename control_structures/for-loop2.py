# find max number in list using for loop
x = [10,20,30,50]

print(max(x))  # built-in function

x = [100,1,200,3]
c = x[0] # assume first value is max
for i in x:
    print(i)
    if i > c:
        print(i)
        c = i
print("max value is:",c)

x = [100,1,200,3]
c = x[0] # assume first value is max
for i in x:
    print(i)
    if i < c:
        print(i)
        c = i
print("min value is:",c)



# create a list using for loop
x =int(input("enter a number:"))
y = range(x)
z = []

for i in y:
    z.append(i)
print(z)


# find the similar values in two lists
x = [10,20,30,40,50]
y = [30,40,50,60,70]

for i in x:
    if i in y:
        print(i)


# find the non-similar values in two lists
x = [10,20,30,40,50]
y = [30,40,50,60,70]

for i,j in zip(x,y):
    # print(i,j)
    if i not in y:
        print(i)
    if j not in x:
        print(j)



# find the non-similar values in two lists
x = [10,20,30,40,50]
y = [30,40,50,60,70]

for i in range(len(x)):
    # print(i,j)
    if x[i] not in y:
        print(x[i])
    if y[i] not in x:
        print(y[i])



