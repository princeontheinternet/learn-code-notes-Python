"""
******** RULES OF ROCK, PAPER OR SCISSORS *************
-------------------------------------------------------------

  Rock wins against scissors.
  Scissors win against paper.
  Paper wins against rock.

"""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_image = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
print(game_image[user_choice])


print("Computer Chooses")

computer_choice = random.randint(0,2)
print(game_image[computer_choice])


if user_choice == 0 and computer_choice == 2:
    print("You Win")
elif user_choice == 1 and computer_choice == 0:
    print("You Win")
elif user_choice == 2 and computer_choice == 1:
    print("You Win")
elif user_choice == computer_choice:
    print("Draw")
else:
    print("You Lose")



"""
    Possible Outcomes

    0:
    U C (U -> User, C -> Computer)
    0 0 (Draw)
    0 1 (goes to else stmt and user loses)
    0 2 (Condition provided in if stmt, user wins)

    1:
    1 0 (Condition provided in if stmt, user wins)
    1 1 (Draw)
    1 2 (goes to else stmt and user loses)

    2:
    2 0 (goes to else stmt and user loses)
    2 1 (Condition provided in if stmt, user wins)
    2 2 (Draw)
"""