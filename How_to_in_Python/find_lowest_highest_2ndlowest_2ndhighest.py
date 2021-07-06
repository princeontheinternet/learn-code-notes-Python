list1 = [4, 1, 2, 2, 1, 3, 4, 2, 5, 5, 1, 6, 5, 9]

# unique elements
print(set(list1))

# lowest element
print(sorted(list(set(list1)))[0])

# second lowest element
print(sorted(list(set(list1)))[1])

# highest element
l = len(set(list1))
print(l)    # TODO: Remove after testing
print(sorted(list(set(list1)))[l-1])

# second highest element
print(sorted(list(set(list1)))[len(set(list1))-2])
