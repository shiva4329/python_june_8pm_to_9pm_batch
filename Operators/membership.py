# Membership operators in python ---> used to test whether a value or variable is found in a sequence (string, list, tuple, set, dictionary)
# in , not in

x = 'python programming'    # string

print('p' in x)  # True ---> checks whether 'p' is present in the string x or not
print('z' in x)  # False ---> checks whether 'z' is present in the string x or not
print('g' not in x)  # False ---> checks whether 'g' is not present in the string x or not 
print('y' not in x)  # True ---> checks whether 'y' is not present in the string x or not

y = [10,20,30,40,50]   # list
print(20 in y)  # True ---> checks whether 20 is present in the list y or not
print(25 in y)  # False ---> checks whether 25 is present in the list y or not
print(30 not in y)  # False ---> checks whether 30 is not present in the list y or not
print(60 not in y)  # True ---> checks whether 60 is not present in