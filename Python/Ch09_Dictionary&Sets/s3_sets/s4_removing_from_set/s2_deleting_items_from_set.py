# Removing items from set

# A set of 10 int
small_ints = set(range(6))
print(small_ints)           # {0, 1, 2, 3, 4, 5}

# small_ints.clear()
# print(small_ints)         # This will remove all the items

# small_ints.discard(4)     # removes 4
# small_ints.remove(3)      # removes 3
# print(small_ints)

# small_ints.discard(99)    # if item is not there it will not do anything
# print(small_ints)
#
# small_ints.remove(99)     # if item is not there it will give error
# print(small_ints)
