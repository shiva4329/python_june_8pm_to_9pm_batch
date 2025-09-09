# if - else condition : when stmt/condition gets staisfies 
#                   then only it will allow to execute the block of code
#                   if not goes to else block


x = 10
if x > 5:
    print('if condition is satisfied')
    print("x is greater than 5")
else:
    print('if condition is not satisfied')
    print("x is lesser than 5")




x = 1
if x > 5: # not satisfied bcause 1 is not greater than 5 then it will go to else block
    print('if condition is satisfied')
    print("x is greater than 5")
else:
    print('if condition is not satisfied')
    print("x is lesser than 5")



# check if x value is even or odd
x = 5  
if x % 2 == 0:# 5 is odd number so it will go to else block bcoz 5%2 is not equal to 0 
        # the if condition is not satisfied
    print("x is even number")
else:
    print("x is odd number")




# check if real-time, if a student percentage is greater than 40 then he is pass otherwise fail

std_per_ip = 60
if std_per_ip > 40: # 60 is greater than 40 so the if condition is satisfied
    print("Student is pass")
else:
    print("Student is fail")



std_per_ip = 40
if std_per_ip > 40: # 60 is greater than 40 so the if condition is satisfied
    print("Student is pass")
else:
    print("Student is fail")


std_per_ip = 40
if std_per_ip >= 40: # 60 is greater than 40 so the if condition is satisfied
    print("Student is pass",std_per_ip)
else:
    print("Student is fail")



# check if patient temperature is greater than 98 then he is fever otherwise normal
# tmr assignement 

# x = 99

# x = 97.9

