""" f = open("demo.txt", "w")
f.write("I want to learn java script tommarow")
#print(data)
f.close()
#print(type(data))

f = open("demo.txt", "r")
data = f.read(10)
print(data)
f.close()
print(type(data)) 

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

    with open("demo.txt", "w") as f:
        f.write("new data")

        import os

        os.remove("sample.txt") """
def check_for_line():
    word = "java"
    data = True
    line_no = 1

    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()

            if word in data:
                print(line_no)
                return

            line_no += 1

    return -1

print(check_for_line())