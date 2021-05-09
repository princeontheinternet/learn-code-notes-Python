#                   Section 3: Slicing With Negative Numbers


# 0   |1   |2   |3   |4   |5   |6   |7   |8  |9   |10   |11  |12   |13
# N   |o   |r   |w   |e   |g   |i   |a   |n  |    | B   |l   |u    |e
# -14 |-13 |-12 |-11 |-10 |-9  |-8  |-7  |-6 |-5  |-4   |-3  |-2   |-1

parrot = "Norwegian Blue"

# Normal Slicing with Negative Nos.
# if step value is not negative treat the slicing as normal slicing
#   (and you can't go backward from starting position in normal slicing (where step_value is not given))

print(parrot[-4:2])     # This wont work as we are going backward in normal slicing
print(parrot[-4:12])    # This works as 12 comes ahead and now back in slicing
print(parrot[-4:])      # Blue (start with -4 and extend up-to the default last char)
print(parrot[-1:])      # e (start with -1 and extend up-to the default last char)
print(parrot[:1])       # N (start with default first char and extend up-to 1 but not including 1
print(parrot[0])        # N (normal indexing)
