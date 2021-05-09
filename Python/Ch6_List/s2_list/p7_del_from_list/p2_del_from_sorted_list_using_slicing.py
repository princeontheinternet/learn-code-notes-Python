# This program is faster than the other two as it deletes all the elements once by slicing.
# whereas other two program traverse backward and delete elements one by one.

data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging
del data[:stop]
print(data)


# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):  # slicing backward
    if data[index] <= max_valid:
        # We have the index of the last item to keep.
        # Set 'start' to the position of the first
        # item to delete, which is 1 after 'index'.
        start = index + 1
        break

print(start)  # for debugging
del data[start:]
print(data)

#   Output:

# 2
# [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
# 14
# [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191]
