# Use a for loop to produce list of ints, rather than list of str.
# You can either modify the contents of the 'values_list' list in place,
#   or create a new list of ints.

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']

values = "".join(generated_list)
print(values)   # 9 223 372 036 854 775 807

values_list = values.split()    # splits based on default argument i.e. space
print(values_list)  # ['9', '223', '372', '036', '854', '775', '807']

# 1st Method replace the values in place
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)  # [9, 223, 372, 36, 854, 775, 807]

# 2nd Method create a new list. (This method is slow)
new_list = []
for value in values_list:
    new_list.append(int(value))

print(new_list)     # [9, 223, 372, 36, 854, 775, 807]


