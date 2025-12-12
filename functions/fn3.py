# few exampes with fn


# find a given number is even or odd using function:

def check_num():
    x = 10
    if x%2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")


check_num()


# def check_num():
#     x = int(input("Enter x value : "))
#     if x%2 == 0:
#         print(f"{x} is even")
#     else:
#         print(f"{x} is odd")


# check_num()


# with paramter

def check_num(x):
    if x%2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

a = 150
check_num(a)