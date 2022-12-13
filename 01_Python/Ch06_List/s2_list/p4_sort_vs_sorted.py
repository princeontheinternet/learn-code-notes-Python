# s.sort() vs sorted()

# s.sort():
# s.sort() is a "list method" which sorts the list.
# s.sort() sorts the original list.

# sorted():
# sorted() is a "built-in python function" which also sorts the list.
# sorted() creates a copy of the list and sorts the list.

number = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]

sorted_number = sorted(number)
print(sorted_number)  # gives sorted list. It creates a new list.
print(number)  # gives original unsorted list

number.sort()  # gives sorted list
print(number)  # number list has been changed to sorted list.

# sorting in descending order:
# number.sort(reverse = True)   # using sort()
# sorted_number = sorted(number, reverse=True)  # using sorted()

# case-insensitive sorting:
names = ["Graham", "John", "terry", "eric", "Terry", "michael"]
names.sort(key=str.casefold)  # using sort()
print(names)
# sort_names = sorted(names, key=str.casefold)  # using sorted()
# print(names)

#   Output

# [1.6, 2.3, 3.1, 4.5, 8.7, 9.2]
# [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
# [1.6, 2.3, 3.1, 4.5, 8.7, 9.2]
# ['eric', 'Graham', 'John', 'michael', 'terry', 'Terry']
