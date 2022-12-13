# Taking i/p from user and replacing the list values

# Displaying the list
def display_game(game_list):
    print(f"Here is the game list: {game_list}")


# User valid input
def position_choice(game_list):
    choice = ''

    while choice not in game_list:

        choice = int(input(f"Pick a position to replace: "))

        if choice not in game_list:
            print(f"Sorry, {choice} position doesn't exist")

    return choice


# Replacement
def replacement_choice(game_list, position):

    user_replacement = input(f"Type a string to place at {position} position: ")

    game_list[position] = user_replacement

    return game_list


def game_on_choice():
    choice = ''

    while choice.casefold() not in ['y', 'n']:

        choice = input("Would you like to keep playing? (y or n)")

        if choice.casefold() not in ['y', 'n']:
            print("Please make sure you type the right i/p.")

    if choice.casefold() == 'y':
        return True
    else:
        return False


gl = [0, 1, 2]
game_on = True

while game_on:

    # 1. Display the list
    display_game(gl)

    # 2. Take user input for the position
    position = position_choice(gl)

    # 3. Replaced field
    gl = replacement_choice(gl, position)

    display_game(gl)

    # 4. Continue the game or not
    game_on = game_on_choice()