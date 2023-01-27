# del keyword and pop method

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# Removing items from dictionary using del keyword.
del [fruit["apple"]]
print(fruit)

# Deleting the full dictionary
# del fruit


# Removing items using dict.pop()
# --> dictionary.pop(keyname, defaultvalue)
# If the default value is not mentioned and if the key is not present then an error comes.

result = fruit.pop("apple", "Not present")  # If the key is not present it will return the default value.
print(result)

# Removing items using dict.popitem()
result1 = fruit.popitem() # removes the last item
print(result1)


# Removing all items using dict.clear(), it retunrs None.
fruit.clear()

# -----------------------------------
# Dictionaries do not have remove method
fruit.remove()
# The above line will give AtttributeError.
# ----------------------------------------