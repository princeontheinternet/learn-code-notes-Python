d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']


d2 = {
    7:  "lucky seven",
    10: "ten",
    3:  "this is the new three",
}


# .KEYS()
""" .keys() Method - It returns view object. The view object contains the keys of the dictionary, as a list.
    Syntax: dictionary.keys() 
"""
# *********************************************************************************************************************
# keys method returns the keys of the dictionary
keys = d.keys()
print(keys)

for item in d.keys():  # If you write .keys this means that you must be dealing with dict keys.
    print(item)  # even if u don't write .keys it will give the same o/p but .keys helps to understand that we want keys
    # It is a good way to read a program.


# .VALUES()
""" .values() Method - It returns a view object. The view object contains the values of the dictionary, as a list.
    Syntax: dictionary.values()
"""
# *********************************************************************************************************************
v = d.values()
print(v)


# .ITEMS()
""" .items() Method - It returns view object. It contains the key-value pairs of the dictionary, as tuples in a list. 
    Syntax: dictionary.items()
"""

for i, j in d.items():
    if j == "four":
        print(f"{d[i]} was found with the key {i}")  # four was found with the key 4


# .FROMKEYS()
""" dict.fromkeys() - The fromkeys() method returns a dictionary with the specified keys and the specified value.
    Syntax: dict.fromkeys(keys, value)  
    default value for value is None.
 """
# **********************************************************************************************************************
# From dict class we are calling an object fromkeys which will pass the keys
# and give them default value of 0 to a new_dict

# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)


# .UPDATE()
""" .update() method - The update() method inserts the specified items to the dictionary. 
     Syntax: dictionary.update(iterable)
"""
# *********************************************************************************************************************
# print(d.update(d2))   # Returns None
d.update(d2)

for key, value in d.items():
    print(key, value)








