# Lambda Functions

"""
--> It is a built-in function.
--> A lambda function is a small anonymous function.
--> A lambda function can take any number of arguments, but can only have one expression.

Syntax ---> lambda arguments : expression
-->The expression is executed and the result is returned:

"""

# def check_even(num):
#     return num % 2 == 0
check_even = lambda num: num % 2 == 0

my_num = [1, 2, 3, 4, 5, 6, 7]

# print(list(filter(check_even, my_num)))
print(list(filter(lambda num: num % 2 == 0, my_num)))


#######################################################


name = ['Ram', 'Laxman', 'Bharat', 'Shatrughan']

# 1st char of the names
print(list(map(lambda x: x[0], name)))      # ['R', 'L', 'B', 'S']

# Reverse of all the names
print(list(map(lambda x: x[::-1], name)))   # ['maR', 'namxaL', 'tarahB', 'nahgurtahS']
