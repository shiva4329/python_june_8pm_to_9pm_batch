# if - elif condition : when stmt/condition gets staisfies 
#                   then only it will allow to execute the if block of code
                    # otherwise it will go to elif block
#                   if elif condition gets satisfied then it will execute elif block of code
#                   if not goes to 
# else block




x = 10
if x > 15: # if condition is not satisfied because 10 is not greater than 15
    print("if condition is satisfied")
elif x > 5: # elif condition is satisfied because 10 is greater than 5
    print("elif condition is satisfied")
else:
    print("if and elif conditions are not satisfied")


x = 5
if x > 15: # if condition is not satisfied because 10 is not greater than 15
    print("if condition is satisfied")
elif x > 5: # elif condition is satisfied because 10 is greater than 5
    print("elif condition is satisfied")
else:
    print("if and elif conditions are not satisfied")




x = 10.1 # check the type of value is int(x is int) or not(not int)
print(type(x)) # it will print the type of value

if type(x) == int: # if condition is satisfied because x is int
    print("x is int type value")
elif type(x) == str: # elif condition is not satisfied because x is not str
    print("x is str type value")
elif type(x) == float: # elif condition is satisfied because x is float
    print("x is float type value")
else:
    print("x is not int type value")



#
# check if given input is between 1 to 10 then it is valid otherwise print not in range

x = int(input("Enter a number: "))
if x > 1:
    print("x is greater than 1")
elif x < 10:
    print("x is less than 10") 
else:
    print("x is not in range")



x = int(input("Enter a number: "))
if x > 1:
    print("x is greater than 1")
if x < 10:
    print("x is less than 10") 
else:
    print("x is not in range")



x = 100
if x > 1 and x < 10:
    print("x is in range")
else:
    print("x is not in range")



x = 100
if x > 1 or x < 10:
    print("x is valid")

else:
    print("x is not in range")


x = 29

if x > 1 and x < 10:
    print("x is below 10")

elif x > 10 and x < 20:
    print("x is below 20")

elif x > 20 and x < 30:
    print("x is below 30")
else:
    print("x is not in range")



x = 29

if x > 1 and x < 10:
    print("x is below 10")

elif x > 10 or x < 20:
    print("x is below 20")

elif x > 20 and x < 30:
    print("x is below 30")
else:
    print("x is not in range")



x = 29

if x > 1 and x < 10:
    print("x is below 10")

if x > 10 or x < 20:
    print("x is below 20")

if x > 20 and x < 30:
    print("x is below 30")
else:
    print("x is not in range")



# leap year logic
# 09/11 - exercise - check if a year is leap year or not
# year = 1996
