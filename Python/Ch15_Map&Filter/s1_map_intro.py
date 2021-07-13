# Map Function


"""
MAP() Function:
    map(function, iterables)

1. The map() function executes a specified function for each item in an iterable.
2. The item is sent to the function as a parameter.
3. Return type of map function is object address.
"""

text = "What have Romans ever done for us"


# Capitalizing each char in text using list comprehension
capitals = [each_char.upper() for each_char in text]
print(capitals)

print("*" * 90)

# Capitalizing each char in text using Map function
map_capitals = list(map(str.upper, text))  # when you pass a function as an argument u don't specify parenthesis.
# Therefore, there is no parenthesis for str.upper().
print(map_capitals)


#
#
#


print("----------------------------------------------------------------------")

word_capital = [each_word.upper() for each_word in text.split()]
print(word_capital)


print("*" * 90)


map_word_capital = list(map(str.upper, text.split()))
print(word_capital)
