#                   Section 1: Concatenate String

"""
STRINGS - Strings are ordered sequence of characters that can be indexed and sliced.
ordered means the way things are inserted.
"""

# WAP to take input from user.

greeting = "Hello"
name = input("Please Enter Your Name: ")    # input method is used to take input from user

print(greeting + ", " + name)  # + is used to concatenate strings

# To do the above in one line
print("Hello, " + input("What is your name? ") + "!" )


# Print length of a string
print(len(input("Enter a string whose lenght you want to find? ")))

#   OUTPUT:

# Please Enter Your Name: Prince
# Hello, Prince
# What is your name? Prince
# Hello, Prince!
# Enter a string whose lenght you want to find? Prince
# 6