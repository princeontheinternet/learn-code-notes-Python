# Program to understand the working of range in for loop.

for i in range(1, 11):  # range(start with start value, up-to but not including stop_value)
    print("i is now {}".format(i))

print("*"*80)

for i in range(11):  # range initial value defaults to 0
    print(i)

#   Output:

# i is now 1
# i is now 2
# i is now 3
# i is now 4
# i is now 5
# i is now 6
# i is now 7
# i is now 8
# i is now 9
# i is now 10
# ********************************************************************************
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
