# Getting integer value from user

def get_int(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("Your input is WRONG")


def check_user_input_int_and_within_range(prompt):
    temp = '-'
    within_range = False

    while not temp.isdigit() or not within_range:
        temp = input(prompt)
        # Check User_Input
        if not temp.isdigit():
            print("Wrong Input")

        # Check range
        if temp.isdigit():
            if int(temp) in range(0, 10):
                within_range = True
            else:
                print('Out of range')
                within_range = False
    return int(temp)


def check_only_user_input_int(prompt):
    temp = ''

    while not temp.isdigit():
        temp = input(prompt)
        if not temp.isdigit():
            print("Wrong Input")
    return int(temp)


if __name__ == "__main__":

    # ui = get_int("Enter only integer value: ")
    # x = check_user_input_int_and_within_range("Enter a number in range(0,10): ")
    # print(x)
    y = check_only_user_input_int("Enter a number: ")
    print(y)
