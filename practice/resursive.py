def add_sum(lis):
    if str(lis[0]).isalpha():
        return  1 + add_sum(lis[1:])
    else:
        return lis[0] + add_sum(lis[1:])




print(add_sum([1,2,3,'a','b',5]))