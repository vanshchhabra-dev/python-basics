str1= "This is a string. \nMy name is Vansh Chhabra"
print(str1)

#concatenation
str2= "Vansh"
str3= "Chhabra"
print(str2 + " " + str3)
print(len(str1)) #to print length of the string

#indexing
str4="VIPS_College"
print(str4[2]) #to print a specific charachter

#slicing
str5="Btech-VLSI"
print(str5[0:5])
print(str5[6:len(str5)])
print(str5[0:len(str5)])
print(str5[:5])#means[0:5]
print(str5[0:])#means[0:len(str5)]

#negative index
str6="Apple" #A=-5, p=-4, p=-3, l=-2, e=-1
print(str6[-5:-2])

#string functions
str7="i am studying python from apna college"
print(str7.endswith("ege"))
print(str7.capitalize())
print(str7.replace("o", "a"))
print(str7.find("a"))
print(str7.find("q"))
print(str7.count("o"))






