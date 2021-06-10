import pprint


def all_ascii_value(s):
    all_asci = {}
    small = []
    capital = []

    # Building a list of char from A-Z in capital and a-z in small list
    for i in range(26):
        capital.append(chr(ord(s) + i))
        small.append(chr(ord(s.casefold()) + i))

    for char in capital:
        all_asci[char] = ord(char)

    for char in small:
        all_asci[char] = ord(char)

    return all_asci


def check_ascii_value(char: str) -> dict:
    ascii_dict = {char: ord(char)}
    return ascii_dict


choice = ""
while choice != '#':

    print("******** AASCII VALUES ***********")
    print("-> Press 1 for all ascii values")
    print("-> Press 2 for single ascii values")
    print("-> Press # to quit")

    choice = input("Enter your response: ")

    if choice == "#":
        break

    elif choice == '1':
        display_all = all_ascii_value('A')
        pprint.pprint(display_all)

    elif choice == '2':
        user_input = input("Type the char whose ascii value you want: ")
        single_char = check_ascii_value(user_input)
        print(single_char)
        print()
