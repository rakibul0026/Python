
#set  in python
fruits={"apple","banana","mango"}
print(fruits)
print(type(fruits))

#set in set() constructor
fruits=set(["apple","banana","mango"])
print(fruits)
print(type(fruits))

#empty set declare
empty_set=set()
print(type(empty_set))

#search in a set
print("apple" in fruits)
print("water" in fruits)

#Add item to set
fruits.add("Jackfruit")
print("after add element")
print(fruits)

#Remove item from set
fruits.remove("mango")
print("after  remove element")
print(fruits)

#remove use discard
fruits.discard("apple")
print("remove  use discard")
print(fruits)

