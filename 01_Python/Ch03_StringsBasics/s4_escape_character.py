#                   Section 4: Escaped Char

# The o/p will be on 2 different lines so print method by default creates a new line.
print("1. This is first line")
print("This is second line")

# Here we have added a condition in print statement, end the line with space
# instead of going on a new line.
# O/P here will be on same line
print("2. This will continue", end=" ")
print("on same line")

# using \n to go on next line.
print("3. The text will \ngo on next line")

# using \t for tab
print("4. I want tab \t here")

# The string is split over several lines
print("5. This text is too long \
so i want to split in multiple lines \
but the o/p should come in one line. \
Print method should behave as it is.")


#   OUTPUT:

# 1. This is first line
# This is second line
# 2. This will continue on same line
# 3. The text will
# go on next line
# 4. I want tab 	 here
# 5. This text is too long so i want to split in multiple lines but the o/p should come in one line. Print method should behave as it is.
