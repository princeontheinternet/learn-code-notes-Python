# WAP to demonstrate the working of enumerate function.

"""
    What is enumerate function?
        It's a built in function into Python and provide an efficient way to get
        indexes, as well as the values in a loop.

        It creates a tuple of indexes and the values.
"""

for index, character in enumerate("abcdefgh"):
    print(index, character)

for values in enumerate("abcdefgh"):
    print(values)

#   Output:

# 0 a
# 1 b
# 2 c
# 3 d
# 4 e
# 5 f
# 6 g
# 7 h
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
# (5, 'f')
# (6, 'g')
# (7, 'h')
