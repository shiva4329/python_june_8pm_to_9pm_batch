# complex ---> combination of real and imaginary values(a+bj)


x = 10+5j

print(x)
print(type(x))


#y = 0+j # error bcoz of imaginary part should not be empty

#print(y)
#print(type(y))



y = 1j # returns only imaginary part
print(y)
print(type(y))




# extracting real and imaginary part

a = 10+11j

print(a.real) # returns the real part with decimal value
print(a.imag)# returns the imaginary part with decimal value



a = 10.1+11.05j

print(a.real) # returns the real part with decimal value
print(a.imag)# returns the imaginary part with decimal value
