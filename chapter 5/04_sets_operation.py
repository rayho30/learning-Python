a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union -> All unique elements
print("Union:", a | b)

# Intersection -> Common elements
print("Intersection:", a & b)

# Difference -> Elements in a not in b
print("Difference:", a - b)

# Symmetric Difference -> Non-common elements
print("Symmetric Difference:", a ^ b)

# Subset
c = {1, 2}
print(c.issubset(a))

# Superset
print(a.issuperset(c))

# Disjoint
d = {7, 8}
print(a.isdisjoint(d))