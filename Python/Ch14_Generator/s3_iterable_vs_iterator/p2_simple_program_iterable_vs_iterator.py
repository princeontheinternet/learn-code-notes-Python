# Program to demonstrate Iterable vs Iterator

my_list = ["Monday", "Tuesday", "Wednesday", "Friday", "Saturday", "Sunday"]


# Normal for loop using Iterable
for i in my_list:
    print(i)

print("*"*90)


# For loop using Iterator
for i in iter(my_list):
    print(i)

print("*"*90)


# Using iter and next in one piece
my_iterator = iter(my_list)     # List has now become iterator i.e. now I can use next() func

for i in range(0, len(my_list)):
    next_element = next(my_iterator)    # using next() on iterator
    print(next_element)