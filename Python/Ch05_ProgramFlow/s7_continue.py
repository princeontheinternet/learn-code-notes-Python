#                   Section 7: Continue Statement

# Continue statement executes the next iteration of the loop
#   and doesn't executes the remaining part of the loop.

# WAP to print all nos from 0-20 that aren't divisible by 3 or 5 using continue statement.

for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        continue                    # if it is divisible then continue to next loop else print it.
    print(i)


#   Output:

# 1
# 2
# 4
# 7
# 8
# 11
# 13
# 14
# 16
# 17
# 19
