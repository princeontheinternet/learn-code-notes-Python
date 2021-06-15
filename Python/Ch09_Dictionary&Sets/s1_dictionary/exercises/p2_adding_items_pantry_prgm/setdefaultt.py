from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")


"""
dictionary.setdefault(keyname, value)

1. setdefault method returns the value of the key, if the key exists.
2. chicken_quantity variable holds the value of the key passed to the setdefault method.
3. The key here is chicken which exists in dict. Therefore it's value is shown.

4. If the key doesn't exist it will give the default value passed to the method.
5. *** It also adds the default value and the key to the dict *** 
"""


# here beans will be added to dict with "beans": 0, key:value
beans_quantity = pantry.setdefault("beans", 0)
print(beans_quantity)

print(pantry)


# get method also does the same i.e. it gives the value of the key
# and if the key doesn't exist it gives the default value that has been passed.
# but it does not add that to dictionary

ketchup_quantity = pantry.get("ketchup", 0)
print(f"Available ketchup:  {ketchup_quantity}")

# ketchup will not be added to dict as we have used get method.
