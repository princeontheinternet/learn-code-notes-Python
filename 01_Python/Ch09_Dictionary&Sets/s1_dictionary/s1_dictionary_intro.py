# Dictionary Intro

"""

    1. Dictionaries are Mapping Data Type.

    2. Dictionaries preserver the Order of Insertion but are accessed using Keys and not Index.
            ● As of Python version 3.7, the keys will appear in the order they were added.
        ● In Python 3.6 and earlier, dictionaries are unordered.

    3. Dictionaries are Mutable.
        1. Therefore, Dictionaries are Addable and Changeable.

    4. Dictionaries do not allow Duplicates. If duplicated, the latest values will be updated.

    5. Dictionaries are used to store data values in {"key":"value"} pairs.

    6. Dictionary use hash codes which makes them faster to access the key and value.

"""


# 1. Creating a Dictionary
fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
print(id(fruit))  # 2743597275584

print()
print("********** ACCESSING DICTIONARY *******")

# 1. Accessing the Dictionary using key
print(fruit["lemon"])  # o/p --> a sour, yellow citrus fruit


# 2. Accessing the Dictionary using get method
print(fruit.get("orange", "key is not present"))    # dict.get(key, default = None)


# If the key doesn't exist then get method will return None or the default value that has been passed.

# get method is useful when you are not sure whether the key is present
# as the normal passing keys gives error if key is not present but this is faster.




