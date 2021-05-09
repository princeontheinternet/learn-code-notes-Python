#                    Section 4: Join Method

"""
    Join():
        1. It is a "String Method"
        2. The join() method takes all items in an iterable and joins them into one string.
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
