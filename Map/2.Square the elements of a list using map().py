#2.Square the elements of a list using map()
def square(x):
    return x*x
num=[1,2,3,4,5]
result=list(map(square,num))
print(result)
