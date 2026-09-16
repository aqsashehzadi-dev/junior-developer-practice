def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"


students = [
    {"name": "Aqsa", "marks": 75},
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 55},
    {"name": "Ahmad", "marks": 40}
]

while True:
    print("1. View Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Exit")
    print("5. Delete Student")

    choice = input("Enter your choice: ")

    if choice == "1":
        for student in students:
            grade = calculate_grade(student["marks"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Grade:", grade)
            print()

    elif choice == "2":
        name = input("Enter student name: ").strip()

        if not name:
            print("Name cannot be empty!")
            continue

        duplicate = False

        for student in students:
            if student["name"].lower() == name.lower():
                duplicate = True
                break

        if duplicate:
            print("Student with this name already exists!")
            continue

        try:
            marks = int(input("Enter student marks: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if 0 <= marks <= 100:
            students.append({"name": name, "marks": marks})
            print("Student added successfully!")
        else:
            print("Marks must be between 0 and 100!")
    elif choice == "3":
        name = input("Enter student name to search: ").strip()

        for student in students:
            if student["name"].lower() == name.lower():
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                print("Grade:", calculate_grade(student["marks"]))
                break
        else:
            print("Student not found!")

    elif choice == "5":
        name = input("Enter student name to delete: ")

        for student in students:
            if student["name"].lower() == name.lower():
                students.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")