# Day 4: Dictionaries Practice
# Topics:
# - creating dictionaries
# - adding/updating values
# - looping over dictionaries
# - simple applications

print("---- Program 1: Student Marks ----")
students = {}

n = int(input("How many students? "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nAll students:", students)

print("\n-----------------------------\n")

print("---- Program 2: Search student ----")
search_name = input("Enter name to search: ")

if search_name in students:
    print(search_name, "marks:", students[search_name])
else:
    print("Student not found ❌")

print("\n-----------------------------\n")

print("---- Program 3: Class average ----")
total = 0

for mark in students.values():
    total += mark

if len(students) > 0:
    print("Class average:", total / len(students))
else:
    print("No students data")

print("\n-----------------------------\n")

print("---- Program 4: Grade distribution ----")
grades = {"A": 0, "B": 0, "C": 0, "D": 0}

for mark in students.values():
    if mark >= 90:
        grades["A"] += 1
    elif mark >= 75:
        grades["B"] += 1
    elif mark >= 60:
        grades["C"] += 1
    else:
        grades["D"] += 1

print("Grade distribution:", grades)
