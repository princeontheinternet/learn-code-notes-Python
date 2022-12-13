# Create a list of even no using List comprehension
even_no_list = [x for x in range(0, 11) if x % 2 == 0]
print(even_no_list)                 # [0, 2, 4, 6, 8, 10]

# Create a list of square of each no
sq_no_list = [x ** 2 for x in range(0, 11)]
print(sq_no_list)                   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Create a list of sq root of each no
existing_list = [144, 169, 196, 225, 256, 289, 324, 361, 400]
sqrt_no_list = [int(x ** 0.5) for x in existing_list]
print(sqrt_no_list)                 # [12, 13, 14, 15, 16, 17, 18, 19, 20]

# Create a list of every 1st word in the string

st = 'Create a list of the first letters of every word in this string'
first_letter_list = [word[0] for word in st.split()]
print(first_letter_list)            # ['C', 'a', 'l', 'o', 't', 'f', 'l', 'o', 'e', 'w', 'i', 't', 's']
