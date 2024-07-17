# list Functions and Methods


# Functions

x = [10,20,30,40,50,60,5]

print(len(x)) # returns the lenth of the list

print(id(x)) # memory address of list

print(sorted(x)) # returns the list in ascending order

print(max(x)) # returns the maximum number in list

print(min(x)) # returns the minimum number in list




# Methods

x = [10,20,30,40,50]
print(x)

#append
x.append(60) # adds the value at end of the list
print(x)

#insert() ---> inserts the value based on position
x.insert(2,200)
print(x)

#pop() ----> deletes the last value
x.pop()
print(x)

#pop(position) ---> deletes the value based on position

x.pop(2)# removes the value at 2nd position

print(x)

# clear() # removes all items in the list (dosent remove the list)
x.clear()
print(x)