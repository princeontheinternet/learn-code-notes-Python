# Sets Intro

"""

    1. Sets are Set Data Type.

    2. Sets are Unordered and Un-Indexed.
        1. Therefore, Sets are Unchangeable.

    3. Sets are Mutable
        1. Therefore, Sets are Addable.

    4. Sets do not allow Duplicates. If duplicated it replaces the existing value and the len(set) doesn't increases.

    5. Sets are written with curly brackets.

    6. Sets also use hash codes which make them faster to access each element



Advantage of SETS

    1. For list and tuples if an element has to be searched then the whole list and tuple has to be accessed.
        but in Sets as it uses hash codes that can be done faster.
        So, membership operator performs faster in sets.

    2. Sets have unique elements

"""

# 1. Creating a set
farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)  # {'cow', 'sheep', 'goat', 'hen', 'horse'}
# Everytime when you will run this the order will change


print()


# 2. Iterating over a set
for i in farm_animals:
    print(i)


print()


# 3. Sets Equality
more_animals = {'sheep', 'goat', 'cow', 'hen', 'horse'}

if more_animals == farm_animals:
    print("The sets are equal")
else:
    print("The sets are different")


print()


# **********************************************

even_list = list(range(0, 10, 2))
even_tuple = tuple(range(0, 10, 2))
even_dict = dict.fromkeys((range(0, 10, 2)))
even_set = set(range(0, 10, 2))

print(f"Even list: {even_list}")
print(f"Even tuple: {even_tuple}")
print(f"Even dict: {even_dict}")
print(f"Even set: {even_set}")

