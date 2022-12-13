import random


# 1. Shuffle List
def shuffle_list(game_list):
    random.shuffle(game_list)  # shuffle method returns None. So we created our function that returns shuffled list.
    return game_list


# 2. User Guess --> We can also take ref from Z_Miscellaneous get_integer function
def user_guess():
    guess = ''
    while guess not in [0, 1, 2]:
        guess = int(input("Pick a number 0, 1, 2: "))
    return guess


# 3. check_guess
def check_guess(game_list, guess):
    attempt = 1

    if game_list[guess] == 'o':
        print(f"CONGO!!!! You got in right in {attempt}st attempt.")
        print(f"Shuffled list = {game_list}")
    else:
        while game_list[guess] != 'o':
            print("wrong")
            attempt += 1
            guess = user_guess()
        print(f"you got in right in {attempt} attempt.")
        print(f"Shuffled list = {game_list}")


# 1. Initial list
my_list = ['', 'o', '']

# 2. Shuffling
shuffled_list = shuffle_list(my_list)

# 3. User input
user_input = user_guess()

# 4. Check guess
check_guess(shuffled_list, user_input)
