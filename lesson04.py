# fullName = input("Enter your full name: ")

# # delete spaces from the full name
# fullName = fullName.strip()

# print("Your full name is:", fullName)
# print("Your full name has", len(fullName), "characters")
# print("Your full name has", len(fullName.split()), "words")
# print("Your full name in uppercase is:", fullName.upper())


# ------------------------------------

# import numbers
# numbers = []

# for i in range(5):
#     number = int(input("Enter a number: "))
#     numbers.append(number)

# print("The numbers you entered are:", numbers)
# print("The sum of the numbers is:", sum(numbers))
# print("The average of the numbers is:", sum(numbers) / len(numbers))
# print("The maximum number is:", max(numbers))
# print("The minimum number is:", min(numbers))
# print("The absolute values of the numbers are:", [abs(num) for num in numbers])


# ------------------------------------

# def calculate_average(grades):
#     if len(grades) == 0:
#         return 0
#     return sum(grades) / len(grades)

# def get_grade_letter(average):
#     if average >= 90:
#         return 'A'
#     elif average >= 80:
#         return 'B'
#     elif average >= 70:
#         return 'C'
#     elif average >= 60:
#         return 'D'
#     else:
#         return 'F'

# grades = input("Enter grades separated by spaces: ")
# grades_list = list(map(int, grades.split()))
# average_grade = calculate_average(grades_list)
# grade_letter = get_grade_letter(average_grade)

# print(f"The average grade is: {average_grade:.2f}")
# print(f"The letter grade is: {grade_letter}")


# ------------------------------------

def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

def get_grade_letter(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

countStudents = int(input("Enter a number to count down from: "))

for i in range(countStudents, 0, -1):
    name = input("Enter a student's name: ")
    grades = input(f"Enter {name}'s grades separated by spaces: ")

    if grades.strip() == "":
        print(f"No grades entered for {name}. Skipping.")
        continue

    student_grades = list(map(int, grades.split()))
    average_grade = calculate_average(student_grades)
    grade_letter = get_grade_letter(average_grade)
    max_grade = max(student_grades)
    min_grade = min(student_grades)

    # print all the information for the student
    print(f"\n{name}'s average grade is: {average_grade:.2f}")
    print(f"{name}'s letter grade is: {grade_letter}")
    print(f"{name}'s maximum grade is: {max_grade}")
    print(f"{name}'s minimum grade is: {min_grade}\n")