# Write data
with open("rayhan.txt", "w") as f:
    f.write("Hello Rayhan!\n")
    f.write("Welcome to Python.")

# Read data
with open("rayhan.txt", "r") as f:
    print(f.read())

# Append data
with open("rayhan.txt", "a") as f:
    f.write("\nThis is appended text.")

# Read again
with open("rayhan.txt", "r") as f:
    print("\nUpdated File Content:")
    print(f.read())