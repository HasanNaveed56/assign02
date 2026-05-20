# Data Types
name = "Hasan"        # String
age = 16              # Integer
height = 5.7          # Float
is_student = True     # Boolean

print(name)
print(age)
print(height)
print(is_student)


# IF Statement
age = 18

if age >= 18:
    print("You are eligible to vote")


# IF-ELSE Statement
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")


# ELIF Statement
marks = 75

if marks >= 80:
    print("A Grade")
elif marks >= 60:
    print("B Grade")
elif marks >= 40:
    print("C Grade")
else:
    print("Fail")


# Nested IF-ELSE
age = 20
has_id = True

if age >= 18:
    if has_id == True:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Not allowed (under 18)")


# Simple Logic Building
num = 10

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


# Even or Odd
num = 7

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Login System
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")