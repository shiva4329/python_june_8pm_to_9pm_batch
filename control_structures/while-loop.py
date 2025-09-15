# while loop == iterates until the condition is true, if condition is false it will terminate

# while True: # infinite loop
#     print("hello")

x = True
while x:
    print("hello")
    x = False

# print 1 to 10 using while loop
 
x = 0
while x <= 10:
    print(x)
    x += 1

# print even numbers from 1 to 20 using while loop
x = 0
while x <= 20:
    if x % 2 == 0:
        print("even number:",x)
    x += 1


# stop the while loop untill user gives the 'stop' command
x = input("enter a command:")
while x != 'stop':
    print("hello")
    x = input("enter a command:")


# print 10 to 1 using while loop
x = 10
while x >= 1:
    print(x)
    x -= 1


x = [10,20,30,40,50] # print all the values in the list using while loop
i = 0
while i < len(x):
    print(x[i])
    i += 1

x = 'python programming' # print all the vowels in the string using while loop
# find factorial of 5 using while loop and for loop
# check whether the given number is armstrong number or not using while loop and for loop
