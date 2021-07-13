# Nested List Comprehension.
# Using for loop in list comprehension to access the elements of list comprehension
# USing generator with list comprehension

# For Loop code
for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)

print("*"*90)


# For looping list comprehension
for table_tuple in [(i, i * j) for i in range(1, 11) for j in range(1, 11)]:
    print(table_tuple)

print("*"*90)


# Unpacking tuple in for loop of list comprehension
for x, y in [(i, i * j) for i in range(1, 11) for j in range(1, 11)]:
    print(x, y)


print("*"*90)
print("\nGENERATOR\n")

# Always use this code as this is generator and wont occupy space for every element,
# Generator will only occupy space for the next element.
for x, y in ((i, i * j) for i in range(1, 11) for j in range(1, 11)):
    print(x, y)

