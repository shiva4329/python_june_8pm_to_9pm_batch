# if condition : when stmt/condition gets staisfies 
#                   then only it will allow to execute the block of code


x = 10

if x > 5:
    print('if condition is satisfied')
    print("x is greater than 5")

x = 2
if x > 5:
    print('if condition is satisfied')
    print("x is greater than 5")



x = 10  # check if x value is even or odd
if x % 2 == 0:
    print("x is even number")


# check if real-time input is even or odd number
x = int(input("Enter any number: "))
if x % 2 == 0:
    print("x is even number")