#                   Section 1: Indexing

# WAP to print "we win" from the string "Norwegian Blue".

# 0   |1   |2   |3   |4   |5   |6   |7   |8  |9   |10   |11  |12   |13
# N   |o   |r   |w   |e   |g   |i   |a   |n  |    | B   |l   |u    |e
# -14 |-13 |-12 |-11 |-10 |-9  |-8  |-7  |-6 |-5  |-4   |-3  |-2   |-1

parrot = "Norwegian Blue"

# print we win using positive index
print(parrot[3], end="")
print(parrot[4], end="")
print(parrot[9], end="")
print(parrot[3], end="")
print(parrot[6], end="")
print(parrot[8], end="")

print()

# print we win using negative index
# Formula:
# *** [positive_index - total_length] ***
print(parrot[3 - 14], end="")
print(parrot[4 - 14], end="")
print(parrot[9 - 14], end="")
print(parrot[3 - 14], end="")
print(parrot[6 - 14], end="")
print(parrot[8 - 14], end="")

#   OUTPUT:

# we win
# we win
