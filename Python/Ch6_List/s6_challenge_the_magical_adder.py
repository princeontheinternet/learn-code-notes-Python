# WAP which prompts users to enter three nos separated by ",".
# Your program should calculate(a+b+c) and display the result.

user_input = input("Enter three nos separated by ',': ")

split_user_input = user_input.split(",")
# print(split_user_input)

int_user_input = []
for values in split_user_input:
    int_user_input.append(int(values))

a, b, c = int_user_input

print("Your result is {}.".format(a + b + c))
