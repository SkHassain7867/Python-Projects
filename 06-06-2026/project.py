import os

FILE = "students.txt"


def add_student():
    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    course = input("Enter course: ").strip()

    if not name or not age or not course:
        print("All fields are required ❌")
        return

    with open(FILE, "a") as f:
        f.write(f"{name},{age},{course}\n")

    print("Student added ✅")


def view_students():
    if not os.path.exists(FILE):
        print("No records found ❌")
        return1
 
    with open(FILE, "r") as f:
        data = f.readlines()

    if not data:
        print("No students available ❌")
        return

    print("\n--- Student List ---")
    for i, line in enumerate(data, start=1):
        try:
            name, age, course = line.strip().split(",")
            print(f"{i}. Name: {name}, Age: {age}, Course: {course}")
        except ValueError:
            continue   # skip bad lines


def search_student():
    keyword = input("Enter name to search: ").strip().lower()

    if not os.path.exists(FILE):
        print("No records found ❌")
        return

    found = False

    with open(FILE, "r") as f:
        for line in f:
            try:
                name, age, course = line.strip().split(",")
                if keyword in name.lower():
                    print(f"Found → Name: {name}, Age: {age}, Course: {course}")
                    found = True
            except ValueError:
                continue

    if not found:
        print("Student not found ❌")


def delete_student():
    keyword = input("Enter name to delete: ").strip().lower()

    if not os.path.exists(FILE):
        print("No records found ❌")
        return

    with open(FILE, "r") as f:
        lines = f.readlines()

    new_lines = []
    found = False

    for line in lines:
        try:
            name, age, course = line.strip().split(",")
            if keyword not in name.lower():
                new_lines.append(line)
            else:
                found = True
        except ValueError:
            continue

    with open(FILE, "w") as f:
        f.writelines(new_lines)

    if found:
        print("Student deleted ✅")
    else:
        print("Student not found ❌")


# ================= MENU =================
while True:
    print("\n==== Student Management System ====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting... 👋")
        break
    else:
        print("Invalid choice ❌")