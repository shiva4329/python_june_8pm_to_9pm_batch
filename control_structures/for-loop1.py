# for loop - iterates finite times based on input

x = 'python'
for i in x:
    print(i)


x = [10,20,30,40,50]
for i in x:     
    print(i)

x = (10,20,30,40,50)
for i in x:     
    print(i)

x = {10,20,30,40,50}
for i in x:    
    print(i)



x = range(0,10)
print(x)
for i in x:     
    print(i)


for i in range(0,10):     
    print(i)   

for i in range(0,100,20):     
    print(i)



x = [10,20,30,40,50]

for i in range(len(x)):     
    print(i)   # it will print index values





x = [10,20,30,40,50]
for i in range(len(x)):     
    print(x[i]) 


x = [1,2,3,4,5,6,7,8,9,10] # find the even values
for i in range(len(x)):     
    print(x[i])
    if x[i] % 2 == 0:
        print("even number:",x[i])


# using above try for vowels in a string
x = 'python programming'


