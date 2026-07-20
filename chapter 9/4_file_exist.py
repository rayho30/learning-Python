import os

if os.path.exists("ray.txt"):
    print("File exists")
else:
    print("File not found")