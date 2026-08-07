"""class Student:

    def __init__(self, fullname):
       self.name = fullname
       print("Adding new student in data base")
    


s1 = Student("Hassain")
print(s1.name)

s2 = Student("imran")
print(s2.name)

#_____________________________

 class Student:
    def __init__(self, name):
        self.name = name

# Create objects
s1 = Student("Hasaain")
s2 = Student("Imran")

# Print names
print(s1.name)
print(s2.name)

#_____________________________

class car:
    color = "blue"
    brand = "mercedes"

car1 = car()
print(car1.color)
print(car1.brand) """

class student:
 
 college_name = "ABC college"
 name = "anonymouse"

 def __init__(self, name, marks):
    self.name = name
    self.marks = marks
    print("Adding new student in data base")
    

s1 = student("Hassain", 98)
print(s1.name)
print(s1.marks)