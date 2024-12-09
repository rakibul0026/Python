#1. Write a Python program to triple all numbers in a given list of integers.
def multi(x):
    return x+x+x
nums = [1, 2, 3, 4, 5, 6, 7]
result=list(map(multi,nums))
print(result)
