p1 = "subscribe this"
p2 = "buy now"
p3 = "click this"

message =input("Enter your comment: ")

if(p1 in message or p2 in message or p3 in message):
    print ("This comment is spam")
else:
    print("this comment not spam")