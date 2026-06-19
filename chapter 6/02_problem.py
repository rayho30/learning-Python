sub1 =int(input("Enter marks 1st sub: "))
sub2 =int(input("Enter marks 2nd sub: "))
sub3 =int(input("Enter marks 3rd sub: "))

total_percentage = (100*(sub1+sub2+sub3))/300

if(total_percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("You are pass with", total_percentage)

else:
    print("you are failed,Try again", total_percentage)