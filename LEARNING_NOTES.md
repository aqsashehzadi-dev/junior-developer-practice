# Learning Notes

This file contains the Python, Git, and GitHub concepts I have practiced during my junior developer preparation.

## Git & GitHub

- `git status` — checks the current working tree and branch status.
- `git add` — stages changes for the next commit.
- `git commit` — saves staged changes as a commit.
- `git push` — sends local commits to GitHub.
- `git pull` — gets and integrates updates from GitHub.
- `git branch` — shows or creates branches.
- `git switch` — switches between branches.
- `git merge` — combines changes from one branch into another.
- `git log --oneline` — shows commit history in a compact form.
- `.gitignore` — prevents selected files, such as `.env`, from being tracked.
## Weekly Review

### Learned
- 

### Built
- 

### Solved
- 

### Improved
- 

### Achieved
- 

### Shared
- 

### Next
- 
## Python Basics

- Variables store data such as names and numbers.
- `input()` gets information from the user.
- `int()` converts text input into an integer.
- `if / elif / else` is used for decisions.
- `for` and `while` loops repeat code.
- Lists store multiple values.
- Dictionaries store key-value pairs.
- Functions make code reusable.
- `return` sends a value back from a function.
- `try / except` handles errors.
- `open()` is used to read and write files.
- Modules such as `math` provide additional functionality.


### 1. Functions

I learned how to create and use functions in Python.

Example:

```python
def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
```

A function helps organize code into a reusable block.

### 2. Conditional Statements

I practiced `if`, `elif`, and `else` to make decisions based on conditions.

I used conditions to:

* Calculate student grades
* Validate marks
* Check student names
* Handle menu choices

## Python Data Structures

### 3. Lists

I learned how to store multiple students in a list.

```python
students = [
    {"name": "Aqsa", "marks": 75},
    {"name": "Ali", "marks": 85}
]
```

I also practiced:

```python
students.append(...)
students.remove(...)
```

`append()` adds a new item to a list, while `remove()` removes an existing item.

### 4. Dictionaries

I practiced dictionaries to store student information using key-value pairs.

Example:

```python
{"name": "Aqsa", "marks": 75}
```

I accessed dictionary values using keys:

```python
student["name"]
student["marks"]
```

## Loops

### 5. While Loop

I used a `while True` loop to keep the student management menu running until the user chooses Exit.

```python
while True:
    ...
```

### 6. For Loop

I used `for` loops to go through the students list and perform operations such as:

* Displaying students
* Searching for a student
* Checking duplicate names
* Deleting a student

Example:

```python
for student in students:
    ...
```

### 7. Break and Continue

I learned how to control loops using `break` and `continue`.

`break` stops the loop when the required student is found.

`continue` skips the current iteration and starts the next iteration.

I used `continue` when invalid input was entered while adding a student.

## User Input and Validation

### 8. User Input

I practiced taking input from the user with `input()`.

```python
choice = input("Enter your choice: ")
```

### 9. String Cleaning with `strip()`

I used `.strip()` to remove unnecessary spaces from user input.

```python
name = input("Enter student name: ").strip()
```

### 10. Case-Insensitive Comparison

I used `.lower()` so that student names can be compared without worrying about uppercase or lowercase letters.

```python
student["name"].lower() == name.lower()
```

For example, different capitalization of the same name can still be recognized as the same student.

### 11. Empty Input Validation

I learned how to check whether the user entered an empty student name.

```python
if not name:
    print("Name cannot be empty!")
```

### 12. Duplicate Student Validation

I added validation to prevent two students with the same name from being added.

```python
duplicate = False

for student in students:
    if student["name"].lower() == name.lower():
        duplicate = True
        break
```

If a duplicate is found, the program shows an error message and does not add the student.

### 13. Marks Validation

I learned how to validate student marks.

The program only accepts marks between 0 and 100.

```python
if 0 <= marks <= 100:
    ...
else:
    print("Marks must be between 0 and 100!")
```

## Error Handling

### 14. try and except

I learned how to handle invalid numeric input using `try` and `except`.

```python
try:
    marks = int(input("Enter student marks: "))
except ValueError:
    print("Please enter a valid number!")
```

This prevents the program from crashing when the user enters something that cannot be converted into an integer.

## Student Management Features

### 15. View Students

I created a feature to display all students with:

* Name
* Marks
* Grade

### 16. Add Student

I created an Add Student feature that:

1. Takes the student's name.
2. Checks that the name is not empty.
3. Checks for duplicate names.
4. Takes the student's marks.
5. Validates the marks.
6. Adds the student to the list if all validations pass.

### 17. Search Student

I created a Search Student feature that searches for a student by name.

If the student exists, the program displays:

* Name
* Marks
* Grade

If the student does not exist, it displays:

```text
Student not found!
```

### 18. Delete Student

I created a Delete Student feature.

The program searches for the student by name and removes the matching student from the list.

If the student does not exist, it displays:

```text
Student not found!
```

### 19. Grade Calculation

I created a reusable function to calculate grades based on marks.

| Marks    | Grade |
| -------- | ----- |
| 80–100   | A     |
| 60–79    | B     |
| 50–59    | C     |
| Below 50 | Fail  |

## Menu-Driven Program

I learned how to create a simple menu-driven application.

The program provides options for:

1. View Students
2. Add Student
3. Search Student
4. Exit
5. Delete Student

The menu continues running until the user selects Exit.

## `for...else`

I practiced Python's `for...else` structure while searching for and deleting students.

The `else` block runs when the loop finishes without encountering `break`.

I used this to display:

```text
Student not found!
```

when no matching student exists.

## Git and GitHub

During this project, I practiced the basic Git and GitHub workflow.

### Git Commands Practiced

```bash
git status
git add
git commit
git push
git pull
git log
```

I learned that a common workflow is:

```text
Make changes
    ↓
git status
    ↓
git add
    ↓
git commit
    ↓
git push
```

### Git Concepts Practiced

* Repository
* Working tree
* Staging area
* Commit
* Branch
* Remote repository
* `origin`
* `main` branch
* GitHub synchronization

## Documentation

I practiced documenting my project using:

* `README.md`
* `LEARNING_NOTES.md`

The README explains the purpose and progress of the repository, while the learning notes record the concepts I practiced.

## What I Have Practiced So Far

Through this project, I have practiced:

* Python fundamentals
* Functions
* Conditional statements
* Lists
* Dictionaries
* Loops
* User input
* Input validation
* Error handling
* String methods
* Student data management
* Search functionality
* Delete functionality
* Grade calculation
* Menu-driven programming
* Git
* GitHub
* Project documentation

## Next Learning Goals

I plan to continue improving this project by learning and practicing:

* More advanced Python concepts
* Better code organization
* File handling
* Object-Oriented Programming
* Testing
* Working with APIs
* Building larger projects
* Professional Git and GitHub workflows
