
list1 = [2, 4, 6, 8, 10]
list2 = [1, 3, 5, 7, 9]

print("list1: {}".format(list1))
# id(list)  - id() method returns the object's address in memory.
# is operator can be used to compare the identities of two objects
print("list1_ID: {}".format(id(list1)))

print()

print("list2: {}".format(list2))
print("list2_ID: {}".format(id(list2)))


print("\n***Different ways to create list***\n")
print("1. From existing list")
list3 = list1 + list2
print("list3: {}".format(list3))
print("list3_ID: {}".format(id(list3)))

print()

print("2. From list function")
list4 = list("123456")
print("list4: {}".format(list4))
print("list4_ID: {}".format(id(list4)))

print()

print("3. using .copy method")
list5 = list1.copy()
print("list5: {}".format(list5))
print("list5_ID: {}".format(id(list5)))

# All IDs will be different as we have created new list and also list is MUTABLE.


#   Output:


# list1: [2, 4, 6, 8, 10]
# list1_ID: 140483778152904

# list2: [1, 3, 5, 7, 9]
# list2_ID: 140483778152968

# ***Different ways to create list***

# 1. From existing list
# list3: [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
# list3_ID: 140483778153096

# 2. From list method
# list4: ['1', '2', '3', '4', '5', '6']
# list4_ID: 140483778159496

# 3. using .copy method
# list5: [2, 4, 6, 8, 10]
# list5_ID: 140483778153032
