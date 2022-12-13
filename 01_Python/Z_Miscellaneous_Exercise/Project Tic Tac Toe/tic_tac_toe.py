# TIC TAC TOE PROGRAM

import random


# ####################### FUNCTIONS ####################################


def set_names():
    print("****************** SET NAMES *********************\n")

    first_player = input("Enter Player1 name: ")
    second_player = input("Enter Player2 name: ")
    return first_player, second_player


def choose_first(first_player, second_player):
    print("****************** TOSS TIME *********************\n")

    player1_choice = int(input(f"{first_player} choose a number 0 or 1: "))
    toss = random.randint(0, 1)
    print(toss)  # Todo: remove after testing
    if toss == player1_choice:
        return first_player, second_player
    else:
        return second_player, first_player


def player_input(toss_winner, toss_loser):
    print("****************** CHOOSE MARKER *********************\n")
    marker = ''
    while marker not in ('X', 'O'):
        marker = input(f'{toss_winner}: Choose X or O: ').upper()

    if marker == 'X':
        return 'X', 'O'  # returns a tuple('X', 'O')
    else:
        return 'O', 'X'


def display_board(board):
    print("****************** BOARD *********************\n")
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


def place_marker(board, marker, position):
    board[position] = marker


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or  # across the top
            (board[4] == board[5] == board[6] == mark) or  # across the middle
            (board[1] == board[2] == board[3] == mark) or  # across the bottom
            (board[7] == board[4] == board[1] == mark) or  # down the middle
            (board[8] == board[5] == board[2] == mark) or  # down the middle
            (board[9] == board[6] == board[3] == mark) or  # down the right side
            (board[7] == board[5] == board[3] == mark) or  # diagonal
            (board[9] == board[5] == board[1] == mark))  # diagonal


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# ########################### END OF FUNCTIONS ######################################


# ######################## START OF THE PROGRAM #################################


print("************ WELCOME TO TIC TAC TOE ****************")

while True:

    # 1. Set Names

    p1, p2 = set_names()
    print(f"Player1: {p1}")
    print(f"Player2: {p2}")
    # ################################################################################

    # 2. Toss Time

    toss_winner_player, toss_losing_player = choose_first(p1, p2)

    player1 = toss_winner_player  # player1 will have 1st turn
    player2 = toss_losing_player

    turn = player1

    print(f"CONGO!!!!! {player1} you have won the toss.")
    print(f"{player2} better luck next time.")
    # ##################################################################################

    # 3. Choose X or 0

    winner_marker, loser_marker = player_input(player1, player2)
    print(f"{player1}'s marker: {winner_marker}")
    print(f"{player2}'s marker: {loser_marker}")
    print("*"*50)
    #######################################################################################

    # 4. Create a board
    the_board = [' '] * 10

    # 5.
    print("Let's get started!!")

    game_on = True

    while game_on:

        # PLAYER 1
        if turn == player1:
            # ALGO

            # 1. Show the board
            # 2. Choose a position with the player_choice()
            # 3. Place the marker in that position with the help of place_marker()
            # 4. Check if won then (game_on = False and break while loop)
            # 5. Check if tie using full_board()
            # 6. No tie and no win then turn = player2

            # 1. Show the board
            display_board(the_board)

            # 2. Choose a position
            position = player_choice(the_board)

            # 3. Place the marker
            place_marker(the_board, winner_marker, position)

            # 4. Check Win
            if win_check(the_board, winner_marker):
                display_board(the_board)
                print(f'Congratulations {player1}! You have won the game!')
                print("*********** GAME OVER *************\n")
                game_on = False

            # 5. Check Tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    game_on = False
                # 6. Player 2 turn
                else:
                    turn = player2
        else:
            # PLAYER 2

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, loser_marker, position)

            if win_check(the_board, loser_marker):
                display_board(the_board)
                print(f'Congratulations {player2}! You have won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    game_on = False
                else:
                    turn = player1

    if not replay():
        break
