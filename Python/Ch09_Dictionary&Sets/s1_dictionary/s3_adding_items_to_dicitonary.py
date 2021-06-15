
fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# Dictionaries don't have append method. To add items we have to use new key and value.

print(fruit)
print(id(fruit))

fruit["mango"] = "a very sweet fruit"
print(fruit)
print(id(fruit))

# We noticed that the id of the dictionary didn't change after adding a new items
# this means that dictionaries are Mutable.

