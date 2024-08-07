
x = "cstu" #global variable

def myfunc():
    x = "CSE" # local variable
    print("The value is: " + x)

myfunc()

print("The value is: " + x)
