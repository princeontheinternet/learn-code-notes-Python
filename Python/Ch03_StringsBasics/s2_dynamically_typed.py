#                   Section 2: Dynamically_typed


x = 2
print(x)
print(type(x))

print("-" * 90)

x = "Hello"
print(x)
print(type(x))

# Note:

# Variable: It is just a way to give a meaningful name to an area of memory,
#           into which we can place certain values.
#           Variable and function names should be in lowercase, with words separated by underscore.


# Python is dynamically typed language.

# We don't have to declare the type of a variable i.e. "data type" or
#   manage the memory while assigning a value to a variable in Python.
# This means that the Python interpreter does type checking only as code runs,
#   and the type of a variable is allowed to change over its lifetime.

# Other languages like C, C++, Java, etc..,
#   there is a strict declaration of variables before assigning values to them.


#   OUTPUT:

# 2
# <class 'int'>
# ------------------------------------------------------------------------------------------
# Hello
# <class 'str'>
