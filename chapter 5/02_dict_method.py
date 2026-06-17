info = {
        "Rayhan" : 100,
        "Ariyan" : 50,
        "Aahill" : 90,
        0 :"prome"
}

# print(info.items())
# print(info.keys())
# print(info.values())
# info.update({"Rayhan" :99,"Zayn" :97})
# print(info)

print(info.get("Rayhan")) 
print(info["Rayhan"])

# print(info.get("Rayhan2"))  #output none
# print(info["Rayhan2"])   #output error

# pop() -> Removes a key
info.pop("Ariyan")
print("Pop:", info)

# copy() -> Creates a copy
new_info = info.copy()
print("Copy:", new_info)