# Intersection: Common elements present in both the sets.

# 4. set.intersection()

even = set(range(0, 20, 2))
squares = {0, 4, 16}

print(even)
print(squares)

print(even.intersection(squares))

# 5. set.intersection_update()

even.intersection_update(squares)
print(even)



