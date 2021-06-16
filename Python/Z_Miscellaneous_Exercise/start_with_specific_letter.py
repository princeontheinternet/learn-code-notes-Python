# Printing the word that starts with a specific letter

st = 'Print only the letter that start with S in this sentence using for, split() and if statement'

for word in st.split():    # creates a list of each word separated on the basis of default argument of split i.e. space
    start = word[0].casefold()         # Checks the first letter of the word
    if start == 's':
        print(word)


# Using list comprehension
start_with_s_list = [word for word in st.split() if word[0].casefold() == 's']
print(start_with_s_list)


# Using list comprehension 1st letter of the string
first_letter_of_word_in_string_list = [word[0] for word in st.split()]
print(first_letter_of_word_in_string_list)


# 4 length of word
even_length_word = [word for word in st.split() if len(word) % 4 == 0]
print(even_length_word)
