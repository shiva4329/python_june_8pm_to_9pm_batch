# types of defining fun's

# with-out args

def sample():
    print("with-out args fn")


sample()

# with args fn

def sample(x,y):
    print("with args fn")
    print(f"args are {x},{y}")


sample(10,20)

# non-default args
def sample(x,y):
    print("non-default fn")
    print(f"args are {x},{y}")


sample(10,20)



# default args
def sample(x,y=100): # here givig y value as default with 100, for this when we are not paasing y value to fn call it will take default value
    print("non-default fn")
    print(f"args are {x},{y}")


sample(10)


def sample(x,y=100): # here givig y value as default with 100,
    print("non-default fn")
    print(f"args are {x},{y}")


sample(10,20)


# key word, non keyword
def sample(x,y): # here givig y value as default with 100,
    print("non-default fn")
    print(f"args are {x},{y}")


sample(y = 10,x = 20) # keyword



# 

# def sample(x=100,y): # when definig fn, first need to pass non-default  params
#     print(x,y)


# sample(200)

# # note : parameter without a default follows parameter with a default



def sample(x,y): # when definig fn, first need to pass non-default  params
    print(x,y)


# sample(y = 100,200) # note : positional argument follows keyword argument

sample(200,100)