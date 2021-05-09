# Processing and traversing through nested list.

menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# Print the list and their items which do not have spam in it.
# If spam is there then print count of spam.
for meal in menu:
    if "spam" not in meal:
        print(meal)
        for item in meal:
            print(item)
    else:
        print("{0} has a spam score of {1}"
              .format(meal, meal.count("spam")))

# Output:

# ['egg', 'bacon']
# egg
# bacon
# ['egg', 'sausage', 'bacon']
# egg
# sausage
# bacon
# ['egg', 'spam'] has a spam score of 1
# ['egg', 'bacon', 'spam'] has a spam score of 1
# ['egg', 'bacon', 'sausage', 'spam'] has a spam score of 1
# ['spam', 'bacon', 'sausage', 'spam'] has a spam score of 2
# ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam'] has a spam score of 4
# ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'] has a spam score of 4
