# Number Analyzer

num = int(input("Enter a number to analyze: "))
if num <= 0:
    print("The number is non-positive.")

# Even or Odd
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(f"{num} is {even_or_odd(num)}.")

# Prime Number Check
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Digit Sum
def digit_sum(num):
    return sum(int(digit) for digit in str(abs(num)))

print(f"The sum of the digits in {num} is {digit_sum(num)}.")

# Reverse Number
def reverse_number(num):
    return int(str(abs(num))[::-1]) * (-1 if num < 0 else 1)

print(f"The reverse of {num} is {reverse_number(num)}.")

# Palindrome Check
def is_palindrome(num):
    return str(abs(num)) == str(abs(num))[::-1]

if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

# Digit Count
def digit_count(num):
    return len(str(abs(num)))

print(f"{num} has {digit_count(num)} digits.")