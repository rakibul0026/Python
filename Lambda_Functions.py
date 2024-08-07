# in Normal Function
def calculate(a,b):
 return a*a+2*a*b+b*b
print("Normal Function")
print(calculate(2,4))

#Lambda Functions->Lambda Functions is a function  which was no name
calculate=(lambda a,b:a*a+2*a*b+b*b)(2,3)
print("Use Lambda Functions")
print(calculate)
