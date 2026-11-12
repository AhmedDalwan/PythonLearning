# # User Access Validator
# def can_access(age, is_active, is_banned):
#     if age >= 18 and is_active and not is_banned:
#         return True
#     else:
#         return False

# # try case 5
# print(can_access(20, True, False))  # Expected: True
# print(can_access(17, True, False))  # Expected: False
# print(can_access(25, False, False))  # Expected: False
# print(can_access(30, True, True))  # Expected: False

# ----------------
# Find Student with mark using zip(for searching)
students = ["Alice", "Bob", "Charlie", "David"]
marks = [85, 92, 78, 90]

while True:
    enterName = input("Enter a student's name to find their mark (or type 'exit' to quit): ")
    if enterName.lower() == 'exit':
        print("Exiting the program.")
        break

    found = False
    for name, mark in zip(students, marks):
        if enterName == name:
            print(f"{name}'s mark is: {mark}")
            found = True
            break

    if not found:
        print(f"{enterName} not found.")