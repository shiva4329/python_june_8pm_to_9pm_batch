# using one fn value into another fn value



def age():
    return 50



def details():
    name = 'hello'
    location = 'hyd'
    age_1 = age()

    print(name,location,age_1)

details()