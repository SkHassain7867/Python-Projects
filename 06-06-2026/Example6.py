"""def calc_sum(a, b):
    return a + b

sum = calc_sum(1, 2)
print(sum) 

#________________-----------

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(1, 2, 27)

print("appnacollege" , end=" ")
print("HassainMyhero")  

#---------------------------

cities = ["Andra pradesh", "delhi", "Hyd", "punjab", "jarkhand", "Hyryana"]
heroes = ["prabhas", "nani", "ntr", "surya", "Dhanush"]

print(heroes[0], end= " ")
print(heroes[1], end=" ")

def print_len(list):
    print(len(list))

print_len(cities)
print(len(heroes)) 

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(10) 

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(5) 
#------------------

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("END")

show(5) 

#------------------

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(6)) """

#------------------

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["Apple", "Banana", "graps", "ORANGE"]

print_list(fruits)