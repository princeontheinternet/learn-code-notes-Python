#                   Section 5: String Replacement Field {}

# This program will demonstrate how you can replace variables in a string statement.

age = 23
name = "Prince"

print("{0} is {1} years old".format(name, age))

print()

# You can also use string replacement using the below way
print("{} is {} years old".format(name, age))

print()

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
June: {1}
July: {2}
Aug: {2}
Sept: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))


#     OUTPUT:

# Prince is 23 years old

# Prince is 23 years old

# Jan: 31
# Feb: 28
# Mar: 31
# Apr: 30
# May: 31
# June: 30
# July: 31
# Aug: 31
# Sept: 30
# Oct: 31
# Nov: 30
# Dec: 31
