user_input = input("Enter a number: ")

total = 0

# Only 2 digits number
# print(int(user_input[0]) + int(user_input[1]))

# Dynamic Digit Number
for each_digit in user_input:
    total += int(each_digit)    # Type Conversion

print(total)


'''
Learnings:

1. If I make user_input as integer,
    then I won't be able to use for loop and as integers do not have a defined iteration order and it will give TypeError.

2. Similary if user_input is integer,  
    then I won't be able to use `for each_digit in range(len(user_input))` as int has no len() function.

    Integers cannot be looped as they are not indexed.
'''