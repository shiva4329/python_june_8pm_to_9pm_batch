from functools import reduce
def add(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
res = reduce(add, a)
print(res)



a = filter(lambda x:x>10,[5,10,20,30])

res = reduce(lambda x,y: x+y, list(a))
print(res)