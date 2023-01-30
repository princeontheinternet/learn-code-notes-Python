# Difference: Elements present in one set but not in another.

# 6. set.difference(): 

set1 = set(range(0,10,2))
set2 = set(range(0,10,3))

print(set1)
print(set2)

set3 = set1.difference(set2) 
print(set3)

# 7.  set.difference_updated()
set1.difference_update(set2)
print(set1)


# Symmetric Difference: Unique elements from two sets that are not present in their intersection.

# 8. set.symmetric_difference():  
set3 = set1.symmetric_difference(set2)
print(set3)

# 9 set.symmetric_difference_update()
set1.symmetric_difference_update(set2)
print(set1)
