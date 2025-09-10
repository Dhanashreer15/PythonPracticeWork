from school import students, teachers, results

students.add("Aarav", 101)
students.add("Diya", 102)

teachers.subject("Mrs. Sharma", "Math")
teachers.subject("Mr. Kumar", "Science")

# Display student list
print("Students:")
for s in students.view():
    print(f" {s['roll']}-{s['name']}")

# Display teacher info
print("\nTeachers:")
for t in teachers.view():
    print(f" {t['name']} teaches {t['subject']}")

# Calculate grades
print("\nGrades:")
marks_list = [95, 82, 67, 45, 30]
for i, marks in enumerate(marks_list):
    grade = results.grade(marks)
    print(f"  Student {i+1}: Marks = {marks}, Grade = {grade}")


