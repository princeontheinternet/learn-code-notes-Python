list1 = [1, 3, 7, 9]
list2 = [2, 4, 6, 8]

# 1. METHODS

# 1. append(takes exactly one argument) at the end of the list
list1.append(11)
print(list1)  # [1, 3, 7, 9, 11]

# 2. remove(takes exactly one argument) the item with the specified value
list1.remove(11)
print(list1)  # [1, 3, 7, 9]

# 3. insert(takes exactly 2 arguments: index, object) adds a value to a specified index
list2.insert(0, 0)
print(list2)  # [0, 2, 4, 6, 8]

# 4. count() of a specific item in a list
print(list1.count(3))  # 1

# 5. index(slice/index) of a specific item
print(list1.index(3))  # 1

# 6. sorts the list in place
print(list1.sort())

# 7. clear() removes all the elements
# list1.clear()
print(list1)  # []

# 8. pop() removes the element at the specified position.
# Default argument value is -1 i.e. the last element.
# pop(4)

# 9. extend() adds the list elements (or any iterable) to the end of the current list.
list1.extend(list2)
print(list1)        # [1, 3, 7, 9, 0, 2, 4, 6, 8]

# 2. FUNCTIONS

# 1. Length of list
print(len(list2))  # 5

# 2. Min value in the list
print(min(list2))  # 0
