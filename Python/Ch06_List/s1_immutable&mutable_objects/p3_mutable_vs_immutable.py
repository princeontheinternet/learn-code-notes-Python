# Mutable vs Immutable in terms of object creation and memory management

# Immutable

name = 'prince'
first_name = 'prince'
last_name = 'prince'

print(id(name))
print(id(first_name))
print(id(last_name))

# All the above will have same ids as once object is created the values is shared with the other variables

# Mutable
l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
l3 = [1, 2, 3, 4]

print(id(l1))
print(id(l2))
print(id(l3))

# All the above will have different ids as the value is not shared and everytime a new list is created.
# It is only when we say list1=list2 the ids will be same.
