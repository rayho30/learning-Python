text = "Hello Python World"

print(text.lower())        # hello python world
print(text.upper())        # HELLO PYTHON WORLD
print(text.title())        # Hello Python World
print(text.capitalize())   # Hello python world

print(text.strip())        # Removes spaces from both ends
print(text.replace("Python", "Java"))

print(text.split())        # Split into list
print("-".join(["Hello", "Python"]))

print(text.startswith("Hello"))  # True
print(text.endswith("World"))    # True

print(text.find("Python"))       # Index of Python
print(text.count("o"))           # Count occurrences

print(text.isalpha())     # False (contains spaces)
print(text.isdigit())     # False
print(text.isalnum())     # False (contains spaces)

print(len(text))          # Length of string



name = "  python programming  "

print(name.strip())
print(name.upper())
print(name.lower())
print(name.replace("python", "Java"))
print(len(name))
# These are the string functions you'll use most often in beginner and intermediate Python programs.