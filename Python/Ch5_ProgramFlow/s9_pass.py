#                   Section 9: Pass Statement

# 1. The pass statement is used as a placeholder for future code.
# 2. When the pass statement is executed, nothing happens,
#       but you avoid getting an error when empty code is not allowed.
# 3. Empty code is not allowed in
#       loops, function definitions, class definitions, or in if statements.

number1 = int(input("Enter the 1st number: "))
number2 = int(input("Enter the 2nd number: "))

if number1 > number2:
    # I will get error if I leave this blank. So I will put pass and later decide what I wanna do.
    pass
elif number1 < number2:
    # I will get error if I leave this blank. So I will put pass and later decide what I wanna do.
    pass
else:
    # I will get error if I leave this blank. So I will put pass and later decide what I wanna do.
    pass


#   Output:

# Enter the 1st number: 4
# Enter the 2nd number: 5
