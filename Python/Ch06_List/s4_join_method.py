#                    Section 4: Join Method

"""
    Join():
        1. It is a "String Method"
        2. The join() method takes all items in an iterable and joins them into one string.
        3. It updates the string value in place otherwise
           as string are immutable everytime you add anything to string a new memory address would be required.
"""

flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]

# for flower in flowers:
#     print(flower)

# using join method with separator " || "
print(" || ".join(flowers))

print()

# using join method with separator " "
print(" ".join(flowers))

print()

# using join method with separator ", "
separator = ", "
output = separator.join(flowers)
print(output)

#   Output:

# Daffodil || Evening Primrose || Hydrangea || Iris || Lavender || Sunflower || Tiger Lily
#
# Daffodil Evening Primrose Hydrangea Iris Lavender Sunflower Tiger Lily
#
# Daffodil, Evening Primrose, Hydrangea, Iris, Lavender, Sunflower, Tiger Lily
