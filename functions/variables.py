# types of variables :

# global varaibales ---> declare ouside fn
# local varaibles ---> inside fn



x = 1000 # global

def sample():
    y = 200 # local

    print(x,y)

sample()
# print(x,y) # cannot access local varibale outside fn

# same var with global and local

x = 1000 # global
def sample():
    x = 200 # local

    print(x)

sample()
print(x)


# global keyword

x = 1500 # global
def sample():
    global x # it ovrewrites global value
    x = 3000
    y = 200 # local

    print(x,y)

sample()
print(x)