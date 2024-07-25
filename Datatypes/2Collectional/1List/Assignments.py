# List assignments



x = ['a','b','c','d','e']


# Q1 : display  'b','c','d' using +ve index
print(x[1:4])

# Q2 : display  'b','c','d' using -ve index
print(x[-4:-1])

# Q3 : what will be o/p if x[-2:-4]
print(x[-2:-4])

# Q4 : what will the o/p of x[1:-4]
print(x[1:-4])

# Q5 : what will the o/p of x[-1:-4]
print(x[-1:-4])

# Q6 : what will the o/p of x[:]
#ANS : total list will print

# Q7 : what will the o/p of x[0:5:2]
#Ans : print(x[0:5:2])


#Q8 : x = [10,20,30,40] reverse the list using index
#       o/p = [40,30,20,10]
x = [10,20,30,40]
print(x[::-1])

#Q9 : [100,30,25,5,0,22]  sort the list in both ascending order and descending order
print(sorted(x))
print(reversed(sorted(x)))

for i in reversed(sorted(x)):
    print(i)

y = sorted(x)
print(y[::-1])

#Q10 : [10,50,25,30]  insert the new value '40' at 3rd position
x = [10,50,25,30]
x.insert(3,40)
print(x)

#Q11 : [10,5,11] add the value '15' at last position
x = [10,5,11]
x.append(15)
print(x)

#Q12 : remove the 15 from the list using both index and non-index
# x.remove(15)

x.pop(3)
print(x)
