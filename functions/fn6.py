# calling fun with in another fn

def sample1():
    print("fn 1")


def sample2():
    sample1() # calling one fn in another fn
    print("fn 2")


sample2()