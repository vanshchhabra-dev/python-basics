#WAP to find the greatest of 3 numbers entered by the user

num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))

if((num1>num2) and (num1>num3)):
    print("The greatest number is=", num1)
elif((num2>num1) and (num2>num3)):
    print("The greatest number is=", num2)
elif((num3>num1) and (num3>num2)):
    print("The greates number is=", num3)
print("THANKYOU!")
