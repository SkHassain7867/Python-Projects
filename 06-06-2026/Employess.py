class employee:
    def __init__(self, role, dept, salary):
     self.role = role
     self.dept = dept 
     self.salary = salary

    def showdeatils(self):
       print("role =", self.role)
       print("dept =", self.dept)
       print("salary =",self.salary)

class Engineer(employee):
    def __init__(self, name, age):
       self.name = name
       self.age = age
       super().__init__("Engineer", "cse", "100000")
engg1 = Engineer("Elon Musk", 40)
print("Name =", engg1.name)
print("Age =", engg1.age)
engg1.showdeatils()
