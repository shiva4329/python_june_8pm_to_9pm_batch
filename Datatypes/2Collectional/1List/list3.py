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

#extend() ---> extends the list

x = [10,20,30,40]
print(x)
x.extend([50,60,70,80])
print(x)


#copy() ---> copys the list into another variable

x = [10,20,30,40]
print(x)
y = x.copy()

print(y)

#count() -- returns the occurences of an item in the list

x = [10,20,10,20,30,10]
print(x.count(10))

#index() --- returns the index of the value

x = [10,20,30]
print(x.index(30))

#remove() --- removes the value in list based on value
x = [10,20,30,40,50]
x.remove(40)
print(x)
