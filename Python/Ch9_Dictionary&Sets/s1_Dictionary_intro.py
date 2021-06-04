# Dictionary

"""
1. Dictionaries are used to store data values in {"key":"value"} pairs.
2. Dictionary items are ordered.
    ● As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
3. It does not allow duplicates.
4. The values in dictionary are not accessed by index but by means of keys.
5. Dictionaries are mutable.
"""

# 1. Creating a Dictionary
fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}


print(fruit)
print(id(fruit))

print("*"*90)

# 1. Accessing the Dictionary using key
print(fruit["lemon"])       # o/p --> a sour, yellow citrus fruit

for i in fruit:
    print(i + " --> " + fruit[i])


print("*"*90)

# 2. Keys cannot be duplicated, if duplicated the latest value will be replaced/updated for the key
fruit["lime"] = "good for vitamin C"
print(fruit)


print("*"*90)


# 3. Adding item to Dictionary
fruit["pear"] = "an odd shaped apple"
print(fruit)
print(id(fruit))    # This proves that Dictionaries are mutable as the id's are same even after adding an element.

print("*"*90)

# 4. Removing items from Dictionary using del function
del[fruit["apple"]]
print(fruit)

# Deleting full dictionary
# del fruit
# print(fruit)


print("*"*90)


# 5. Emptying the dictionary using clear method
# fruit.clear()
print(fruit)


print("*"*90)


# 6. Using keys() and values() method.
print(fruit.keys())

print("##### Prining keys #####")
for keys in fruit.keys():
    print(keys)

print()

print(fruit.values())

print("###### Prining Values #####")
for values in fruit.values():
    print(values)

