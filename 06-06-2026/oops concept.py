""" class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your average score is:", sum/3)

# Create object
s1 = Student("Tony Stark", [99, 98, 97])

# Call method
s1.get_avg()

s1.name = "ironman"
s1.get_avg()

class car:
    def __init__(self):
        self.ac = False
        self.acc = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car is Started..")

car1 = car()
car1.start() 

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class Toyotacar(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyotacar("fortuner")
car1 = Toyotacar("Audi")
        
print(car1.color) 

class A:
    varA = "Welcome to my home"

class B:
    varB = "Welcome to my school"

class C(A, B):
    varC = "Welcome to my college"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA) """

class Person:
    name = "Anonymouse"

    def changeName(self, name):
        self.name = name

p1 = Person()
p1.changeName("revanth")
print(p1.name)
print(Person.name)
