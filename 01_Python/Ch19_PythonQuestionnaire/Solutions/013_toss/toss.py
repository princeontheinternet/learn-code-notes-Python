import random

# 1. Using random.randint
coin = random.randint(0, 1) # includes both end points, accepts only integer values.

if coin == 0:
    print("Heads")
else:
    print("Tails")


# 2. Using list and random.choice()
coin = ["Heads", "Tails"]
print(random.choice(coin))


# 3. Using list,index and random.randint()
random_index = random.randint(0, len(coin)-1)
print(coin[random_index])



'''
Learnings:

    1. random.randint(low, high): includes both low and high values and accepts only integer values.
    2. random.choice(seq): Returns random element from a sequence.
'''