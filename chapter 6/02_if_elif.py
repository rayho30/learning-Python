age = int(input("Enter your age : "))

if(age>18):
    print("You are eligible")

elif(age<0):
    print("You are entering invalid negative age")
    
elif(age==0):
    print("invalid")

else:
    print("you are not eligible")

print("End of the program")