my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_popped_list = []

for i in range(len(my_list)):
    my_popped_list.append(my_list.pop())    # pop returns the pop value but append returns None
    # In every loop pop will return the last element and it will be appended to the list.

print(my_list)
print(my_popped_list)


