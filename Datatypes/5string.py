# string : combinaion/group/collection of letters
# string can be defined in single('..')/double(" .. ") in python
# string function in python : str()
# string follows index
#       index : 2types
#               farward index(positive index) --> left to right --> strats from 0
#               backward index(negative index) --> right to left ---> starts from -1


# string defining

x = 'python' # using single quote
print(x)
print(type(x))

# how to print the no of characters/letters of string ---> using len()
print(len(x))

# how to display the memoery address of the variable --> using id()
print(id(x))



# index --> 2 types --> farward and backward

x = "hello"

print(x)

# using +ve index display 'h'
print(x[0])

# using -ve index display 'o'
print(x[-1])

# using +ve index display 'l'
print(x[3])

# using -ve index display 'l'
print(x[-2])

# using -ve index display 'e'
print(x[-4])



# slicing ---> breaking string into smaller pieces
# syntax = x[start position :end position-1]

x = 'python'

print(x)
print(len(x))


#using +ve index display the string 'pyt'

print(x[0:2]) # 't' dosent print bcoz of end position -1 to it will consider 0 to 1 prints 'py'

print(x[0:3])

#using +ve index display the string 'pyth'
print(x[0:4])

# using +ve index display the string 'th'
print(x[2:4])

# using -ve index display the string 'on'
print(x[-2:-1]) # returns only 'O' bcoz endposition-1 so in our scenario -1-1 = -2 inthat case it will display only one letter/char
print(x[-2:]) # when we are giving ending position as empty it will treated as infinity so it will display to end of the string

# note : starting position should be lesser than ending position


y = 'Welcome to India'

print(y[:5]) # returns from begining to 5-1th index

print(y[5:]) # returns 5th index to end of the string

print(y[:]) # retunrs to total string


# how to print string in reverse order using index
# syntax: [st:end:step size]

x = 'hello'

print(x[::-1]) # returns the string in reverse order

print(x[::2]) # retunrs the every 2nd char in the str
