# check the user input value is palindrome or not


def palindrome(val):
    print(val)
    val = str(val)
    if val == val[::-1]:
        print(f"{val} == {val[::-1]:} is palindrome")

x = input("Enter value : ")
palindrome(x)


# find the value is prime number or not using python fn's