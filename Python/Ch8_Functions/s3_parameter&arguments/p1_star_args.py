# Explanation of *args

numbers = (0, 1, 2, 3, 4, 5)

print(numbers, sep=";")         # (0, 1, 2, 3, 4, 5)
print(*numbers, sep=";")        # 0;1;2;3;4;5

# 1. When you use asterisk before an object it unpacks the sequence i.e it will take zero or more no of arguments.

# here *number was unpacked and the unpacked values were passed to print function.
# something like print(*numbers) = print(0, 1, 2, 3, 4, 5)

# 2. Therefore, *args represents an unpacked tuple.
# 3. It is usual to use a plural name for *args.

print(0, 1, 2, 3, 4, 5, sep=";")    # 0;1;2;3;4;5


def test_star(*args):
    print(args)     # (0, 1, 2, 3, 4, 5)
    for x in args:
        print(x)    # prints one by one in new line.


test_star(0, 1, 2, 3, 4, 5)

print()
test_star()
