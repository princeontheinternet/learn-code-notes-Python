# Intro to nested list.

even = [2, 4, 6, 8, ]
odd = [1, 3, 5, 7, 9, ]

numbers = [even, odd]
print(numbers)  # [[2, 4, 6, 8], [1, 3, 5, 7, 9]]

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)

#   Output

# [[2, 4, 6, 8], [1, 3, 5, 7, 9]]
# [2, 4, 6, 8]
# 2
# 4
# 6
# 8
# [1, 3, 5, 7, 9]
# 1
# 3
# 5
# 7
# 9
