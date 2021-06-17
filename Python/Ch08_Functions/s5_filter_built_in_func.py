# Filter() in Python

"""
Mapping -

--> The filter() function returns an iterator
    were the items are filtered through a function to test if the item is accepted or not.

Syntax ------> filter(function, iterable)
"""


def check_even(num):
    return num % 2 == 0


my_num = [1, 2, 3, 4, 5, 6]

print(list(filter(check_even, my_num)))        # [2, 4, 6]
