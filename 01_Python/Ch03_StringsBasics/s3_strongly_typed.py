#                   Section 3: Strongly_typed


age = 23
name = "Prince"

print(name + " is" + age + " years old")  # here int cannot be added with string data type

# Note -
# Strongly typed enforces strict restrictions on intermixing of values with differing data types.
# When such restrictions are violated and error (exception) occurs.


#   OUTPUT:

# print(name + " is " + age + " years old")
# TypeError: must be str, not int
