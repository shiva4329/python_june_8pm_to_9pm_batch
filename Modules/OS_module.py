import os


#listdir : gets the items in the current dir

print(os.listdir())
print(os.listdir("/home/siva/Documents/python_june_8pm_to_9pm_batch/python_june_8pm_to_9pm_batch/Operators"))


#getcwd() : gives the current directoy
print(os.getcwd())

# chdir : directory chnage
# os.chdir("/home/siva/Documents/python_june_8pm_to_9pm_batch/python_june_8pm_to_9pm_batch/Operators")
# print(os.getcwd())

#mkdir :  created the new folder
os.mkdir('new_dir') # Notes : it creates folder whents it is not there

# rmdir : deleted the dir
os.rmdir("new_dir") # Note : it deletes only when folder is empty

