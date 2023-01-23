import random 

names = input("Enter the names separated by comma: ")

list_of_names = names.split(",")

# with random.choice()
# random_person = random.choice(list_of_names)

# without random.choice()
random_person = random.randint(0, (len(list_of_names) - 1))

print(f"{list_of_names[random_person]} needs to pay the bill")


'''
Learnings:

    1. random.randint(low, high): includes both low and high values.

    2. random.choice(seq): Returns a random element from a sequence.
'''