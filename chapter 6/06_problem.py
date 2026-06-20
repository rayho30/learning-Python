marks = int(input("Enter your marks"))

if(marks<=100 and marks>=90):
    print("your grade A+")
elif(marks<90 and marks>=80):
    print("Your Grade A")
elif(marks<80 and marks>=70):
    print("Your Grade A-")
elif(marks<70 and marks>=60):
    print("Your Grade B+")
elif(marks<60 and marks>=50):
    print("Your Grade B")
elif(marks<50 and marks>=40):
    print("Your Grade B-")
elif(marks<40):
    print("Failed")