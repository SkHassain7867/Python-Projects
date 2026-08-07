""" nums = (1, 2, 3, 4, 2, 8, 6)

for el in nums:
 print(el) 
 
 #----------------

seq = range(5)

for i in seq:
 print(i) 

#-------------------
for i in range(2, 101, 2):
  print(i)

for i in range(100, 0, 1):
  print(i) 

#---------------------

n = int(input("Enter a number : " ))

for i in range(1, 21):
 print(n * i) 

#------------------------

n = 7

sum = 0
for i in range(1, n+1):
    sum += i

    print("tota sum =", sum) 

#-----------------------------

n = 3
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("factorial =", fact) """

#--------------------------

n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

    print("factorial =" , fact)