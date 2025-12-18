# function with global variables and local variables values


bal = 0 # global
def bank():
    bal = 100
    name = "SBI" # local
    location = "hyd" #local

    print(name,location,bal)


bank()
# print(bal,name) # local variable
print(bal)




