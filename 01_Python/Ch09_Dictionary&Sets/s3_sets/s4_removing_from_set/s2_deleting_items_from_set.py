# Removing items from set


small_ints = set(range(6))
print(small_ints)           # {0, 1, 2, 3, 4, 5}

# 1. set.clear()
small_ints.clear()
print(small_ints)         # Empty set: set() 

# 2.set.discard()
small_ints.discard(4)     # removes 4
small_ints.discard(99)    # if item is not there it will not raise error


# 3. set.remove()
small_ints.remove(3)      # removes 3
small_ints.remove(99)     # if item is not there it will give error


# 4. del set
del small_ints

# 5. set.pop()
small_ints.pop()    # removes random element and returns that element.