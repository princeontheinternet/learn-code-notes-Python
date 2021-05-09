menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    # Adding ',' in the last list makes it easy to add or remove list
]

# Way 1: we skip spam.
print("\n1st method by directly skipping spam:")

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=", ")  # you can't use sep argument here
            # as there is ony on word. It is used to separate two words
    print()


# Way 2 we del spam using slicing backward.
print("\n2nd method by slicing backward and del spam:")
for meal in menu:
    for i in range(len(meal) - 1, -1, -1):
        if meal[i] == "spam":
            del meal[i]
    print(meal)

# Way 3 using reversed and enumerate function.
print("\n3rd method by using reversed and enumerate function:")

for meal in menu:
    top_index = len(meal) - 1
    for index, value in enumerate(reversed(meal)):
        if value == "spam":
            del meal[top_index - index]
    print(meal)

#   Output


