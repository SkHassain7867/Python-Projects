""" str1 = "This is String. \n we are creating in python"
str2 = "Appna college"
str3 = "welcome to my class"

print(str1,str2,str3)

str4 = "shaik"
str5 = "Hassain"
print(str1+str2)

#-------------------------

num = int(input("Enter number: "))

if (num % 2 == 0):
    print("Even")
else:
    print("Odd") 

a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if(a >= b and a>=c):
    print("first number is largest", a)
elif(b>= c):
    print("second number is largest", b)
else:
    print("third is largest", c) 

#------------------------------
x = int(input("Enter number: "))

if (x % 7 == 0):
    print("Multiple of 7")
else:
    print("Not a multiple of 7") 

student = ["Hassain" , 10.0, "Delhi"]
print(student[0])
student[0] = "Hussain"
print(student) 

list = [2, 1, 3]
print(list.append(4))
print(list.sort(reverse=True))
print(list)

tup = (1, 2, 3, 4, 2, 2)
print(tup.count(2))"""

movies = []
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2st movie: "))
movies.append(("enter 3st movie: "))

print(movies)