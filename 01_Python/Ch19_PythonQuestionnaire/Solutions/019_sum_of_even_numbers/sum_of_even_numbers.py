# Method 1: Using List
even_list = []

for number in range(0, 101, 2):
    even_list.append(number)

print(sum(even_list))


# Method 2: Using total variable
total = 0 
for number in range(0,101,2):
    total += number

print(total)

