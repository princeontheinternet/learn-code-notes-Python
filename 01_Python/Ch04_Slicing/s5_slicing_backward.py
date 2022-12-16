#                   Section 5: Backward Slicing

# Rules -
# [::-1] a negative number should always be attached to indicate backward slicing with step as -1
# 1. start_value should always be greater than the stop_value if both (start & stop value) the integer have same sign.
# 2. start_value will default to end of the string
# 3. stop_value will default to start of string


# 0   |1   |2   |3   |4   |5   |6   |7   |8  |9   |10   |11  |12   |13
# N   |o   |r   |w   |e   |g   |i   |a   |n  |    | B   |l   |u    |e
# -14 |-13 |-12 |-11 |-10 |-9  |-8  |-7  |-6 |-5  |-4   |-3  |-2   |-1

parrot = "Norwegian Blue"

print(parrot[13:0:-1])  # eulB naigewro (N the first letter is not there as stop_value is 0)

print(parrot[-5:-9:-1]) 

print(parrot[-3:2:-1]) # lB naigew
                       # In this case start & stop values have different sign,
                       # therefore, even if the srart value is not greater than stop value, this gives o/p.
                       # As it is possible to go backwards from -3 to 2 in our string.

# Reverse the string
print(parrot[::-1])     # eulB naigewroN
