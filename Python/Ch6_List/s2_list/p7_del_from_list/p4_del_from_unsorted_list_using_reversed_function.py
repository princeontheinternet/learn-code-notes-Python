# reversed():
# reversed() function returns a reversed iterator object.

data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]  # top_index-1 will give right index from starting to del element.

print(data)

#   Output:

# 9 306
# 6 5
# 4 308
# 2 4
# [104, 101, 105, 103, 107, 100, 106, 102, 108]
