# Removing Duplicates in a list

my_list = ["a", "b", "a", "c", "c"]
my_list = list(dict.fromkeys(my_list))
print(my_list)  # ['a', 'b', 'c']

another_list = ["a", "b", "a", "c", "c"]
another_list = list(set(another_list))
print(another_list) # ['a', 'c', 'b']
