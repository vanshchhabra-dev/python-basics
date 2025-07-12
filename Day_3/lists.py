student=["Vansh", 94.25, 18, "VIPS"]
print(student[0])
student[0]="Arjun"
print(student)

#list slicing
marks=[94, 88, 84, 75, 69]
print(marks[1:4])
print(marks[:5])
print(marks[0:])

#list methods
list=[2, 1, 3]
list.append(4)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)

list1=['a', 'd', 'c', 'b']
list1.reverse()
print(list1)

list2=[2, 1, 3]
list2.insert(1,5)
print(list2)

list3=[2, 1, 3, 1]
list3.pop(2)
print(list3)
list3.remove(1)
print(list3)
