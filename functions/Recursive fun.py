# Recursive fun : a function call by it self



def list_sum(lis):
    try:
        if not lis:
            return 0
        else:
            return lis[0] + list_sum(lis[1:])
    except:
        print("Error occured")


total = list_sum([10,20,30])
print("total sun",total)



def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))




# function with in functio
def sample1():
    return 10
def sample2():
    return 20

def total():
    return sample1() + sample2() + 30


print(total())