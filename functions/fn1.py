# defining sample fn in python


# create a sample addition fn


def sample_add():
    x = 10
    y = 20

    print(x+y)


sample_add() #---> fn call




# 

def sample_add():
    x = 10
    y = 20

    print(x+y)



a = sample_add() #---> fn call
print(a)
# note : here we are using only print in fn, so the value is not stored in fn, 
# it just prints the value but not stores the value into fn


# how to store value in fn ---> using return
def sample_add():
    x = 10
    y = 20

    return x+y




a = sample_add() #---> fn call
print(a) # when we are using return value stores fn