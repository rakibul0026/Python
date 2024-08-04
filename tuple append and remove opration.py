fruits=("apple","banana","mango")

fruits=list(fruits)
#append opratiion
fruits[1]="orange"
fruits.append(1)
fruits.append(2)

fruits=tuple(fruits)
print(fruits)

#remove the item in tuple
fruits=list(fruits)
fruits.remove("banana")
fruits=tuple(fruits)
print(fruits)

