import os

name = input("Enter your name: ")

age = (input("Enter your age: "))

if not  age.isnumeric():
    print("Invalid age")
    # terminate
    os._exit(0)
    # sys.exit()

if int (age) >= 18:
    print( name," is an Adult")
else:
    print(name," is a Child")
#lists, booleans, tuples, dictionary, loops