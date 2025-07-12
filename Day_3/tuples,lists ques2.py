#WAP to check if a list contains a palindrome of elements

list=[]
list.append(input("Enter 1st number:"))
list.append(input("Enter 2nd number:"))
list.append(input("Enter 3rd number:"))
print(list)

copy_list=list.copy()
copy_list.reverse()

if(copy_list == list):
    print("PALINDROME")
else:
    print("NOT PALINDROME")
