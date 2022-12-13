# Returning None from functions.


def addition():
    """
    If the return statement has no expression or does not exist itself in the function
    then it returns the None object.

    :return: None
    """
    a = 10
    b = 20
    c = a + b


print(addition())

print()

# Another example.
numbers = [5, 6, 7, 2, 3, 1, 8, 9]
print(numbers)
print(numbers.sort())  # sorts the number in place.
# Returns None
print(numbers)
