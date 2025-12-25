# Identity operators in python ---> used to compare the objects(Address), not the   values  
# is , is not

x = 'python'  # string object 1
y = 'python'  # string object 2
print(id(x))  # address of object x
print(id(y))  # address of object y
print(x is y)  # True ---> both x and y are pointing to same object in memory
print(x is not y)  # False ---> both x and y are pointing to same object




a = [10,20,30]   # list object 1
b = [10,20,30]   # list object 2
print(id(a))  # address of object a
print(id(b))  # address of object b 

print(a == b) # True ---> both a and b have same values
print(a is b)  # False ---> both a and b are pointing to different objects in memory even though the values are same
print(a is not b)  # True ---> both a and b are pointing to different objects

a = (10,20,30)   # tuple object 1
b = (10,20,30)   # tuple object 2
print(id(a))  # address of object a
print(id(b))  # address of object b 
print(a == b) # True ---> both a and b have same values
print(a is b)
print(a is not b)
