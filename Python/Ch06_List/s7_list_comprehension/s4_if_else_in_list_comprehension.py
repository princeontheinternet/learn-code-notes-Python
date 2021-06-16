# If else in list_comprehension

k = [f'{x} --> even' if x % 2 == 0 else f'{x} --> odd' for x in range(0, 11)]
print(k)

# Also see W3Schools example
