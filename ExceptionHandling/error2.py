#how to display the error type

try: # anything by 0 isinfinity so try block throws error
    x = 10
    y = 10/0
    print(y)

except Exception as ex: # except cathes
    print(ex)



try:
    z == 10    
except Exception as ex: # except cathes
    print(ex)