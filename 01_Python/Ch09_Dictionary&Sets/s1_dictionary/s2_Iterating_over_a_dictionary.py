# Use of items method explained.

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# This only returns key
# for i in fruit:
#     print(i, fruit[i], sep=" --> ")


# using items_method
print(fruit.items())
# dict_items([('orange', 'a sweet, orange, citrus fruit'), 
# ('apple', 'good for making cider'), 
# ('lemon', 'a sour, yellow citrus fruit'), 
# ('grape', 'a small, sweet fruit growing in bunches'), 
# ('lime', 'a sour, green citrus fruit')])

for i, j in fruit.items():
    print(i, j, sep=" --> ")

# items method returns an iterator of tuples, and we have unpacked it using i, j.



