#                   Section 2: is Operator


# "is" and "is not" operators are known as "Identity operators".
# is operator checks whether both the operands refer to the same object or not.

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content as lists are mutable.


print(x == y)
# to demonstrate the difference between "is" and "==": this comparison returns True because content of x is equal to y


