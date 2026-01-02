# simple Exception handling


# zero division erro


try: # anything by 0 isinfinity so try block throws error
    x = 10
    y = 10/0
    print(y)

except: # except cathes
    print("error occured while doing zero divison")