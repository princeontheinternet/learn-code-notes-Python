fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
# print(fruit["tomato"])  # you will get error as key - tomato is not present in fruit dictionary.


# better way to get the value from a key is using a method i.e. .get() method
while True:
    user_input = input("Enter a fruit or q to exit: ")
    if user_input.casefold() == 'q':
        break
    # elif user_input in fruit:
    #     description = fruit.get(user_input)
    #     print(description)
    # else:
    #     print("{} is not present".format(user_input))

    # get can also take default value for a key, when key is not present.
    description = fruit.get(user_input, "{} is not present".format(user_input))
    print(description)

