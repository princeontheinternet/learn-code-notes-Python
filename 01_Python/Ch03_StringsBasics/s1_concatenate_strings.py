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
print("Hello, " + input("Plese Enter Your Name: ") + "!" ) # Hello, Prince!

#   OUTPUT:

# Please Enter Your Name: Prince
# Hello, Prince
