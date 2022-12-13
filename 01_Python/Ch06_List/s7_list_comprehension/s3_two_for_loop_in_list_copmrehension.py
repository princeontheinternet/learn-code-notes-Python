
# Using Normal Procedure
empty = []
for x in [1, 2, 3]:
    for y in [2, 4, 6]:
        empty.append(x * y)

print(empty)

# two for loop in list comprehension
new_empty = [x*y for x in [1, 2,3] for y in [2, 4, 6]]
print(new_empty)
