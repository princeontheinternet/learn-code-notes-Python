# Getting integer value from user

def get_int(prompt):
    temp = input(prompt)
    if temp.isnumeric():
        return int(temp)
    else:
        print("Your input is WRONG")
        return temp


ui = get_int("Enter only integer value: ")
