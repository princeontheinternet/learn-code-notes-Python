
def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{} is not a valid number".format(temp))


numbers = {}

print(numbers, type(numbers))   # {} <class 'dict'>

numbers = set()

print(numbers, type(numbers))   # set() <class 'set'>

# Duplicates are not allowed in sets
# Adding items to set (distinct)

while len(numbers) < 4:
    # new_value = input("Please enter the next value: ")
    new_value = get_integer("Please enter the next value: ")
    numbers.add(new_value)  # add method is used to add items in a set

print(numbers)

