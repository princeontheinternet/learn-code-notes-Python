# Mapping() in Python

"""
Mapping -

--> It is a built-in function in Python.
--> The map() function executes a specified function for each item in an iterable.
--> The item is sent to the function as a parameter.

Syntax ------> map(function, iterables)
"""


def square_num(num):
    return num ** 2


my_num = [1, 2, 3, 4, 5, 6]

for i in map(square_num, my_num):
    print(i)

print(list(map(square_num, my_num)))        # [1, 4, 9, 16, 25, 36]
