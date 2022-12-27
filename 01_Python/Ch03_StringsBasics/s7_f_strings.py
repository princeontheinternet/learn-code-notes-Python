#                   Section 7: f-strings (formatted strings)


# f-strings (short for "formatted strings") are a new feature in Python 
# that allows you to use variables inside string literals using {}.

name = "Prince"
age = 25

print(f"{name} is {age} years old") # Prince is 25 years old

# If you want to use {{}} inse string literals using formatted strings:

print(f"{{name}}, {{Prince}}") # {name}, {Prince}
