#Add three lists using map function and lambda
num1=[1,2,3]
num2=[2,5,8]
num3=[9,5,1]
print("After the operation:")
print(num1)
print(num2)
print(num3)

result=map(lambda x,y,z:x+y+z,num1,num2,num3)
print("After the operation:")
print(list(result))
