# Set Excercises


# set defining


# empty set

x = {} # when we are giving empty {} it will be treated as empty dict

print(x,type(x))

x = set() # we can create empty set by using set function

print(x,type(x))


# duplicates

x = {10,20,30,10,30,20} # set dosent allow duplicates
print(x)


# Homogenous/heterogeneous values
x = {10,'Hello','Hello',10.20,False,False,10+3j}
print(x)


#Index 

x = {10,20,30,40}
print(x,len(x))

# print(x[1]) # Error : Set dosent follow index so cannot extract the values with index



