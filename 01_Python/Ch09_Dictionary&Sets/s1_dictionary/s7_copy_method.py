# SHALLOW COPY VS DEEP COPY

# Importing for Deep copy function
import copy

# Copy for immutable items

animals = {
    "lion": "scary",
    "elephant":  "wrinkled",
    "teddy": "stuffed",
}

# things = animals     # here both are referencing to same object. Any change to one of them will reflect in other also.
# print(id(things))     # 2632252660160
# print(id(animals))    # 2632252660160

things = animals.copy()  # here new dict is created. Any change to one of them will not reflect in other.


print(id(things))   # 2575068830336
print(id(animals))  # 2575068830144


things["teddy"] = "toy"

print(things["teddy"])      # toy
print(animals["teddy"])     # stuffed


# *********************************************************************************************************


# COPY FOR MUTABLE ITEMS

animals2 = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

things2 = animals2.copy()

print(id(things2))   # 2575068830336
print(id(animals2))  # 2575068830144

print(things2["teddy"])     # ['cuddly', 'stuffed']
print(animals2["teddy"])    # ['cuddly', 'stuffed']

print(id(things2["teddy"]))     # 2505920225920
print(id(animals2["teddy"]))    # 2505920225920
# IDs are same bcz they are accessing the same list of teddy. Check behind the scenes to understand.

print()

things2["teddy"].append("toy")

print(things2["teddy"])     # ['cuddly', 'stuffed', 'toy']
print(animals2["teddy"])    # ['cuddly', 'stuffed', 'toy']


# ********************************************************************************************************


# BEHIND THE SCENES WITH MUTABLE ITEMS

lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]


animals3 = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}


things3 = animals3.copy()

things3["teddy"].append("toy")


# IDs of both will be same as they are accessing the same list.
print(things2["teddy"])     # ['cuddly', 'stuffed', 'toy']
print(animals2["teddy"])    # ['cuddly', 'stuffed', 'toy']


# The values stored inside the dict aren't list. They are references to lists.
# The list exists somewhere else in memory so if you append an item to the list and
#    # you have use copy command then both the dict will have the new item
# This is called shallow copy as the list are not copied to new dict instead it copies the references.
#   # So, any item added to the list, it gets added to both dict.
# SHALLOW COPY: COPIES REFERENCES


# ********************************************************************************************************


# DEEP COPY

animals3 = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

things3 = copy.deepcopy(animals3)

things3["teddy"].append("toy")

print(things3["teddy"])     # ['cuddly', 'stuffed', 'toy']
print(animals3["teddy"])    # ['cuddly', 'stuffed']

# DEEP COPY creates separate memory location for each list here.
print(id(things3["teddy"]))     # 2208027466752
print(id(animals3["teddy"]))    # 2208027466432
