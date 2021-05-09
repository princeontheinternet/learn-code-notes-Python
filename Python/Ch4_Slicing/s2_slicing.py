#                   Section 2: Slicing

# Slicing -
# variable[start_value:stop_value]
# start with start_value and extend up to "stop_value" but not including "stop_value"


# 0   |1   |2   |3   |4   |5   |6   |7   |8  |9   |10   |11  |12   |13
# N   |o   |r   |w   |e   |g   |i   |a   |n  |    | B   |l   |u    |e

parrot = "Norwegian Blue"

print(parrot[0:6])              # Norweg
print(parrot[3:5])              # we

print(parrot[0:9])              # Norwegian
print(parrot[:9])               # Norwegian (default start_value is the first char in string)

print(parrot[10:14])            # Blue
print(parrot[10:])              # Blue (default stop_value is the last char in string)

print(parrot[:])                # Norwegian Blue (default start and stop)

print(parrot[:6] + parrot[6:])  # Norwegian Blue

