# write a python program to print all content from directories

import os

directory = "/Go lang"

for root, dirs, files in os.walk(directory):
    print(f"\nDirectory: {root}")

    for d in dirs:
        print(f"[DIR]  {d}")

    for f in files:
        print(f"[FILE] {f}")