# Exception handling with finally

# finally : it will executes the finaally block  either error occured or not occured

# Ex: file operetion, 

try:
    x = 100
    y = 100
    print(x+y)

except Exception as e:
    print(e)

finally:
    print("Execution completed")




try:
    x = 100
    y = "hello"
    print(x+y)

except Exception as e:
    print(e)

finally:
    print("Execution completed")