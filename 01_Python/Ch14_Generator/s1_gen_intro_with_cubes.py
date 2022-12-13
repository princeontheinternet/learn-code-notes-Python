# Generators

# This def will save the cubes in the list. This will take space and not memory efficient
def create_cubes_using_func(n):
    result = []

    for x in range(n):
        result.append(x ** 3)
    return result


# This will not occupy memory.
def gen_cubes_using_generator(n):
    for x in range(n):
        yield x ** 3


# ################### End of Function ###################


# Calling normal method
for cube in create_cubes_using_func(10):
    print(cube)

print(create_cubes_using_func(10))  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# calling using generator
for gen in gen_cubes_using_generator(10):
    print(gen)

print(gen_cubes_using_generator(10))  # <generator object gen_cubes_using_generator at 0x000002746A819580>

# You have to iterate through the function in generator if you want the cubes as it is not storing it.
