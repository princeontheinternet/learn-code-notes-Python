#                   Section 1: Immutable Objects

# There are two types of Objects in Python -

# 1. Mutable - whose state or content can be changed.
#         Eg -  list, dict, set, bytearray

# 2. Immutable - whose state or content can't be changed.
#         Eg - int, float, bool, string, tuple, frozenset, bytes

# Below program will demonstrate the working of immutable objects

name = "prince"
first_name = name
# first_name = "prince"     This statement will also give same id as once the object is created value is shared.

print(name)                 # prince
print(id(name))             # 140167348388168
# id(): id() method returns the object's address in memory.

print(first_name)           # prince
print(id(first_name))       # 140167348388168


name += " rathore"

print(name)                 # prince rathore
print(id(name))             # 140167324441200 --> id got changed as it created new object and assigned the value to it.

print(first_name)           # prince --> as 1st name object has prince and the 2nd name object has prince rathore
print(id(first_name))       # 140167348388168
