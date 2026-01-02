# how to handle partucular error : only handle ZeroDivisionError , else go to main Exception


try:
    x = 100
    y = x//0

except ZeroDivisionError:
    print("occured ZeroDivisionError: denominator should not be zero")

except Exception:
    print(Exception)



try:
    x = 100
    y = int(input("Enter y valye :"))

    print(x//y)

except ZeroDivisionError:
    print("occured ZeroDivisionError: denominator should not be zero")

except Exception:
    print(Exception,"Other Error")
    raise Exception