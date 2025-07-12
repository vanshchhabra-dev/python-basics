light= "green"

if(light == "green"):
    print("You may GO")
elif(light == "red"):
    print("You should STOP")
elif(light == "yellow"):
    print("You should WAIT")
else:
    print("Light is Broken")

#nesting
age=int(input("Enter age:"))
if(age>=18):
    if(age>=80):
        print("Too much old to drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")


