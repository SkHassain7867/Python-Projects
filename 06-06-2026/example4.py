""" marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

x = int(input("enter che : "))
marks.update({"chem" : x})

print(marks)
#----------------------

i = 1
while i <= 100:
    print("Hello world", i)
    i+=1 

#----------------------

i = 5

while i >= 1:
    print(i)
    i -= 1

print("Loop ended") 

#----------------------

n = int(input("Enter a number : "))
i = 1
while i <= 10:
 print(4*i)
 i += 1 """

#---------------

i = 1
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue 
    print(i)
    i += 1