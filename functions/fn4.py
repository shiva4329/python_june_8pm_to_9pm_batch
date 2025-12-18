# check the user input value is palindrome or not


def palindrome(val):
    print(val)
    val = str(val)
    if val == val[::-1]:
        print(f"{val} == {val[::-1]:} is palindrome")

# x = input("Enter value : ")
# palindrome(x)


# find the value is prime number or not using python fn's

# prime number ===? number divides with same or 1
# 2,3,5,7,11,13

#

def findPrimeNumber(val):
    notprime = []
    if val > 1:
        for i in range(2,val):
            if val % i == 0:
                # print(f"{val} is divided by {i}")
                notprime.append(i)
    if notprime:
        print(f"{val} is not prime")
    else:
        print(f"{val} is prime")


    print(notprime)
findPrimeNumber(12)

# find all prime numbers in range :
# ex : 10 ===> 2,3,5,7