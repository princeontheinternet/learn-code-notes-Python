# WAP to print all the separators.

number = "9,223:833,329.3928"
separators = ""

for i in number:
    # isnumeric() is a string method that returns True if all characters in the string are numeric
    if not i.isnumeric():
        separators = separators + i

print(separators)

# Output:

# ,:,.
