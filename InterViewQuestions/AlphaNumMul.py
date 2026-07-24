# perform the multiplication of two alphanumeric strings and return the result as a string
# x = a2b12 -----> o/p :aabbbbbbbbbbbb


x = "a2b3e4"
result = ""

for i in range(len(x)):
    if x[i].isalpha():
        char = x[i]
        num = ""
        j = i + 1
        while j < len(x) and x[j].isdigit():
            num += x[j]
            j += 1
        result += char * int(num)

print(result)