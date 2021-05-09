# del values by traversing backward in the list.

data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

for index in range(len(data) - 1, - 1, - 1):
    if data[index] < min_valid or data[index] > max_valid:
        print(index, data)
        del data[index]

print(data)

#   Output

# 9 [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
# 6 [104, 101, 4, 105, 308, 103, 5, 107, 100, 106, 102, 108]
# 4 [104, 101, 4, 105, 308, 103, 107, 100, 106, 102, 108]
# 2 [104, 101, 4, 105, 103, 107, 100, 106, 102, 108]
# [104, 101, 105, 103, 107, 100, 106, 102, 108]
