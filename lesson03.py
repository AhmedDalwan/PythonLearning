countStudents = int(input("Enter a number to count down from: "))

names = []
grades = []

while countStudents > 0:
    name = input("Enter a student's name: ")
    names.append(name)

    grades = input(f"Enter {name}'s grades separated by spaces: ")
    grades.append(grades)
    countStudents -= 1

for i in range(len(names)):
    student_name = names[i]
    student_grades = list(map(int, grades[i].split()))
    average_grade = sum(student_grades) / len(student_grades)
    print(f"{student_name}'s average grade is: {average_grade:.2f}")
