# WAP to print out capital letters in the string.

quote = """Alright but apart from the Sanitation, the Medicine, Education, Wine, Public, Order, Irrigation, Roads, 
the Fresh-Water System and Public Health, what have the Romans ever done for us? """

for i in quote:
    # isupper() is a string method that returns True if all characters in the string are upper case
    if i.isupper():  # Returns True
        print(i)

print("*" * 80)

# OR

for i in quote:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(i)

print("*" * 80)

# OR

letters = ""
for i in quote:
    if i.isupper():
        letters += i  # letters var will store all the characters which have upper case
        # Augmented Assignment (increment by 1 (+=1))
        # letter = letter + 1

print(letters)  # This will just print all the characters in one line

#   OUTPUT:

# A
# S
# M
# E
# W
# P
# O
# I
# R
# F
# W
# S
# P
# H
# R
# ********************************************************************************
# A
# S
# M
# E
# W
# P
# O
# I
# R
# F
# W
# S
# P
# H
# R
# ********************************************************************************
# ASMEWPOIRFWSPHR
