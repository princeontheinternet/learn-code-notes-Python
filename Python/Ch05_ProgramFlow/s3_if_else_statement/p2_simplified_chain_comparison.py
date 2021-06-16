# WAP that takes name and age and prints it.
#   On the basis of age if it is between and including 16 and 65 print work else enjoy.

name = input("Please Enter your name: ")
age = int(input("Please Enter your age: "))

print("\nHi {}, You are {} years old.".format(name, age))


# if age >= 16 and age <= 65:           # This is also right
# if age < 16 or age > 65:               # This is also right using "OR statement"
# if age in range(16,66):

if 16 <= age <= 65:                     # Chain Comaprison
    print("Have a good day at work")
else:
    print("Enjoy")
