#                   Section 1: Mutable Objects


# We can change the value of mutable object without object being destroyed or re-created.

# Below program will demonstrate the working of mutable objects

list1 = [1, 2, 3, 4]
list2 = list1
# list2 = [1, 2, 3, 4]      This will not give the same id. This will create a new list and values will not be shared.

print(list1)            # [1, 2, 3, 4]
print(id(list1))        # 140411219634184
# id(): id() method returns the object's address in memory.

print(list2)            # [1, 2, 3, 4]
print(id(list2))        # 140411219634184


list1.append(5)

print(list1)            # [1, 2, 3, 4, 5]
print(id(list1))        # 140411219634184 --> id did not change

print(list2)            # [1, 2, 3, 4, 5] --> 5 is also added to that list2 as it points to same object.
print(id(list2))        # 140411219634184
