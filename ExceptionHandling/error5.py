# Error handling in function



def sample():
    try:
        x = 100
        y = 200
        z = int(input("Enter Z value : "))
        return x+y/z
    except Exception as e:
        print(f"Exception occure while doing above operation: {e}")
        # sample()
        raise e
    finally:
        print("Function completed")

sample()