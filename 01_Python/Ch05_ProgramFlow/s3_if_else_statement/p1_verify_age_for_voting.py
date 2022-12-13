#                   Section 3: if-else Statement

# WAP for that verifies age for voting.

name = input("Please Enter your name: ")
age = int(input("Please Enter your age: "))

print("\nHi {}, You are {} years old.".format(name, age))

if age >= 18:                               # Using comparison operator
    print("You are eligible for voting")
else:
    print("You are not eligible for voting. Please try after {} years.".format(18-age))
