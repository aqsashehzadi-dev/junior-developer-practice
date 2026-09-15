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
    ("Aqsa", 75),
    ("Ali", 85),
    ("Sara", 55),
    ("Ahmed", 40)
]

for name, marks in students:
    grade = calculate_grade(marks)
    print("Student:", name, "| Marks:", marks, "| Grade:", grade)