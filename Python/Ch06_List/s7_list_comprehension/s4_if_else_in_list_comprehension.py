# If else in list_comprehension

k = [f'{x} --> even' if x % 2 == 0 else f'{x} --> odd' for x in range(0, 11)]
print(k)

# only if: here if will be after for loop as it doesn't have any else statement
even_no_list = [x for x in range(0, 11) if x % 2 == 0]
print(even_no_list)


# Also see W3Schools example
