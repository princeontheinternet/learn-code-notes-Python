import random

coin = random.randint(0, 1) # includes both end points

if coin == 0:
    print("Heads")
else:
    print("Tails")



'''
Learnings:

    1. random.randint(low, high): includes both low and high values.
'''