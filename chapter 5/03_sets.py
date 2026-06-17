# Creating a set
numbers = {1, 2, 3}

# add() -> Add one item
numbers.add(4)
print("add:", numbers)

# update() -> Add multiple items
numbers.update([5, 6, 7])
print("update:", numbers)

# remove() -> Remove an item (error if not found)
numbers.remove(7)
print("remove:", numbers)

# discard() -> Remove item (no error if not found)
numbers.discard(10)
print("discard:", numbers)

# pop() -> Remove a random item
numbers.pop()
print("pop:", numbers)

# copy() -> Copy set
new_set = numbers.copy()
print("copy:", new_set)

# clear() -> Remove all items
temp = {1, 2, 3}
temp.clear()
print("clear:", temp)