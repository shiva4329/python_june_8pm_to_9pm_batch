
# Assignment operators:

# = ---> assiging value
# += -----> addition with assiging
# -+ ------> substraction with assiging
# *= -----> multiplication with assiging
# /=
# //=
# %=
# **=




x = 10 # using assignment operator

y = x+20

print(y)

x = 10
x = x+10 # normal form

print(x)

x = 10
x += 10 # using asignment operators
print(x)



# -=

x = 10
x = x-5

print(x)

x = 10
x -= 5
print(x)


# 09/13
x =[20,10,40,60,50]
op = [10,20,40,50,60] # expected output
# sort the list in ascending order and descending order using only for loop
x = [20,10,40,60,50] # len = 5

for i in range(len(x)): # 0,5
    for j in range(i + 1, len(x)):#0+1 = 1,5
        if x[i] > x[j]:   # swap
            x[i], x[j] = x[j], x[i]

print("Sorted list:", x)

# sum all the values in the list using for loop ex : expected output 10+20+40+60+50 = 180

x = [10, 20, 30, 40]

total = 0
expression = ""   # to build the "10 + 20 + ..." string

for i in range(len(x)):
    total += x[i]             # add each number to total
    if i == len(x) - 1:       # if it's the last element
        expression += str(x[i])
    else:
        expression += str(x[i]) + " + "

print(expression, "=", total)



# method 2
x = [10, 20, 30, 40]
total = 0
for i in x:
    total = total + i

print("sum of all values is:", total)