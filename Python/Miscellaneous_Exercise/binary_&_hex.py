def binary_numbers(number):
    for i in range(number):
        print("{0:>2} in binary is {0:>04b}".format(i))


def hex_numbers(number):
    for i in range(number):
        print("{0:>2} in hex is {0:>03x}".format(i))


user_input = input("Press B for binary conversion and x for hex conversion: ")
n = int(input("Till which number u want to see conversion: "))

if user_input.casefold() == 'b':
    binary_numbers(n)
elif user_input.casefold() == 'x':
    hex_numbers(n)
else:
    print("You entered wrong i/p")
