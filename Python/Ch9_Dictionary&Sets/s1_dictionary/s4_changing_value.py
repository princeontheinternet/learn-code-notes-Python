# del and pop

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "lemon": "a sour, yellow citrus fruit",
         }

# Here, we tried to duplicate lemon key but in o/p only one key would be shown based on the latest value.
# but the order will be same as insertion is preserved.

print(fruit)

# 2. Keys cannot be duplicated, if duplicated the latest value will be replaced/updated for the key
fruit["lemon"] = "good for vitamin C"
print(fruit)
