# Creating a list
fruits = ["apple", "banana"]

# append() -> Adds one item at the end
fruits.append("mango")
print("append:", fruits)

# insert() -> Adds an item at a specific index
fruits.insert(1, "orange")
print("insert:", fruits)

# extend() -> Adds multiple items from another list
fruits.extend(["grape", "kiwi"])
print("extend:", fruits)

# remove() -> Removes the first matching value
fruits.remove("banana")
print("remove:", fruits)

# pop() -> Removes and returns the last item (or item at given index)
fruits.pop()
print("pop:", fruits)

# index() -> Returns the index of a value
print("index of orange:", fruits.index("orange"))

# append() again to demonstrate count()
fruits.append("apple")

# count() -> Counts how many times a value appears
print("count of apple:", fruits.count("apple"))

# sort() -> Sorts the list in ascending order
fruits.sort()
print("sort:", fruits)

# reverse() -> Reverses the list order
fruits.reverse()
print("reverse:", fruits)

# copy() -> Creates a shallow copy of the list
new_list = fruits.copy()
print("copy:", new_list)

# clear() -> Removes all items from the list
temp = [1, 2, 3]
temp.clear()
print("clear:", temp)