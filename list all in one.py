# Create a list of fruits
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# Print the entire list
print(thislist)  # ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

# Print the number of items in the list
print(len(thislist))  # 7

# Print the type of the list
print(type(thislist))  # <class 'list'>

# Print the item at index 1 (second item) in the list
print(thislist[1])  # 'banana'

# Print the last item in the list
print(thislist[-1])  # 'mango'

# Print a slice of the list from index 2 to 4 (inclusive of 2, exclusive of 5)
print(thislist[2:5])  # ['cherry', 'orange', 'kiwi']

# Print a slice of the list from the start to index 3 (inclusive of start, exclusive of 4)
print(thislist[:4])  # ['apple', 'banana', 'cherry', 'orange']

# Print a slice of the list from index 2 to the end
print(thislist[2:])  # ['cherry', 'orange', 'kiwi', 'melon', 'mango']

# Change the item at index 1 to 'blackcurrant'
thislist[1] = "blackcurrant"
print(thislist)  # ['apple', 'blackcurrant', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

# Change items at index 1 and 2 to new values
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)  # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'melon', 'mango']

# Insert 'watermelon' at index 2
thislist.insert(2, "watermelon")
print(thislist)  # ['apple', 'blackcurrant', 'watermelon', 'watermelon', 'orange', 'kiwi', 'melon', 'mango']

# Append 'orange' to the end of the list
thislist.append("orange")
print(thislist)  # ['apple', 'blackcurrant', 'watermelon', 'watermelon', 'orange', 'kiwi', 'melon', 'mango', 'orange']

# Insert 'orange' at index 1
thislist.insert(1, "orange")
print(thislist)  # ['apple', 'orange', 'blackcurrant', 'watermelon', 'watermelon', 'orange', 'kiwi', 'melon', 'mango', 'orange']

# Add elements of a tuple to the list
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)  # ['apple', 'orange', 'blackcurrant', 'watermelon', 'watermelon', 'orange', 'kiwi', 'melon', 'mango', 'orange', 'kiwi', 'orange']

# One way to loop through the list using a for loop with range
for i in range(len(thislist)):
  print(thislist[i])

# Another way to loop through the list using a while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1 

# Sort the list alphabetically (ascending order)
thislist.sort()
print(thislist)  # ['apple', 'banana', 'cherry']

# Sort the list in descending order
thislist.sort(reverse=True)
print(thislist)  # ['cherry', 'banana', 'apple']

# Perform a case-insensitive sort of the list
thislist.sort(key=str.lower)
print(thislist)  # ['apple', 'banana', 'cherry']

# Reverse the order of the list items
thislist.reverse()
print(thislist)  # ['cherry', 'banana', 'apple']

# Make a copy of the list using the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)  # ['apple', 'banana', 'cherry']

# Make a copy of the list using the list() method
mylist = list(thislist)
print(mylist)  # ['apple', 'banana', 'cherry']

# Make a copy of the list using slicing
mylist = thislist[:]
print(mylist)  # ['apple', 'banana', 'cherry']
