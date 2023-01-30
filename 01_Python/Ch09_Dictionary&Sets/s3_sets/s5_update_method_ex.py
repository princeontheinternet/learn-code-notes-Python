# Use the correct method to add multiple items (more_fruits) to the fruits set.
# 2. set.update()d

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)  # updates the set in place and returns None.
print(fruits)   # {'banana', 'mango', 'grapes', 'apple', 'cherry', 'orange'}
