# Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)         # 13
print("Subtraction:", a - b)      # 7
print("Multiplication:", a * b)   # 30
print("Division:", a / b)         # 3.3333
print("Floor Division:", a // b)  # 3
print("Modulus:", a % b)          # 1
print("Exponent:", a ** b)        # 1000

# Comparison Operators
print("Equal:", a == b)           # False
print("Not Equal:", a != b)       # True
print("Greater Than:", a > b)     # True
print("Less Than:", a < b)        # False
print("Greater or Equal:", a >= b)# True
print("Less or Equal:", a <= b)   # False

# Assignment Operators
x = 5
x += 2
print("x += 2:", x)               # 7

x -= 1
print("x -= 1:", x)               # 6

x *= 2
print("x *= 2:", x)               # 12

x /= 3
print("x /= 3:", x)               # 4.0

# Logical Operators
p = True
q = False

print("AND:", p and q)            # False
print("OR:", p or q)              # True
print("NOT:", not p)              # False

# Membership Operators
fruits = ["apple", "banana", "mango"]

print("apple in fruits:", "apple" in fruits)      # True
print("grape not in fruits:", "grape" not in fruits)  # True

# Identity Operators
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)      # True
print("list1 is list3:", list1 is list3)      # False
print("list1 is not list3:", list1 is not list3)  # True