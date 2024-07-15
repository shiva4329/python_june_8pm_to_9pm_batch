# escape sequences = to escape the string for nextline or tab space or converting (') into string

# types of escape sequences:
'''    \n = next-line
        \t = tab space
        \' = returns only '
        \\ = returns only single \
        \\\ = returns only \\   '''


# \n - next line

x = 'India\nJapan'

print(x) # returns in two(India in fist line, Japan in second line) lines


# \t = tab space

x = 'ab'

print(x)

x = 'a\tb'
print(x) # returns string with tabspace in same line


# \'

# display like Ramu's

# x = 'Ramu's' # it will throw an error becoz on (') opostify will treated as ending quote

# How to overcome? using \'

x = 'Ramu\'s'

print(x)

# Ramu's book is with me
x = 'Ramu\'s book is with me'

print(x)


print('\\India\\ is my country')


# assignment

# display : \\Indian's\\ are great human beings

print('\\\\Indian\'s\\\\ are great human beings')
                
