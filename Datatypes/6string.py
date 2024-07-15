# string function and methods


# string functions

x = 'welcome'

print(x)
print(len(x)) # returns the length of str

print(id(x)) # returns the memory address of the value

print(max(x)) # returns maximum character based on ASCII value
print(min(x)) # returns minimum character based on ASCII value

print(sorted(x)) # returns the string in list format ascending order based on ASCII values

print(reversed(x)) # return the value in indirect address(for unpacing need to use for loop)

for i in reversed(x):
    print(i)



# methods

x = 'welcome'

print(x.upper()) # returns the string in  upper case

x = 'HELLO'

print(x.lower()) # returns the string in lower case

x = 'HeLlOn'

print(x.swapcase()) # retunrs the string in swapcase(upper to lower/lower to upper) of each char

x = '    India     '
print(x)

print(x.strip()) # removes the empty spaces from the string

x = '     India     '
print(x)

print(x.rstrip()) # removes empty spaces from right side of the string

print(x.lstrip())# removes empty spaces from left side of the string

x = 'India'

print(x.startswith('I')) # checks the string starts with 'I' or not
print(x.startswith('a'))


print(x.endswith('a'))# checks the string ends with 'a' or not


# assignemt = remaining methods

x = 'hello'
y = '.'.join(x) # seperates the every char with literal
print(y)


x = 'India,Japan,Russia'

print(x.split(','))# splits the string into diff parts and stores in list based on literal we are passing


x = 'abcdefgh'

print(x.split('f'))


# if we want to assign two variables with values in single line using split()


x = 'India,Japan'

a,b = x.split(',')
print(a)
print(b)



x = 'one\\\'s'

print(x)
