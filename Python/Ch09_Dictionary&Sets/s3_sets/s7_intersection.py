# Intersection

# all update method update the set in place whereas other method creates a new set

even = set(range(0, 20, 2))
squares = {0, 4, 16}

print(even)
print(squares)

print(even.intersection(squares))

# subset and superset

if squares.issubset(even):
    print("Square is a Sub-set of even")

if even.issuperset(squares):
    print("Even is superset of square")

# frozenset() is immutable set. So there are no add or remove method as you can't  add things to immutable structures.
