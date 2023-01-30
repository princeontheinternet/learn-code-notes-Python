# superset: contains all the elements of another set, and possibly additional elements.
# subset: contains only elements that are also in another set 
# disjoint: having no common elements.

even = set(range(0, 20, 2))
squares = {0, 4, 16}

if squares.issubset(even):
    print("Square is a Sub-set of even")

if even.issuperset(squares):
    print("Even is superset of square")

# set.isdisjoint(): having no common elements.
print(even.isdisjoint(squares))