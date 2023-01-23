import random
import hangman_arts
from hangman_words import word_list

print(hangman_arts.logo)

chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6

display = ["_" for _ in range(len(chosen_word))]

while True:

    guess = input("Guess a letter")

    for position in range(len(chosen_word)):     
       letter = chosen_word[position]
       if guess == letter:
        display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is a wrong guess. You lose a life !!!!!!")
        lives -= 1
        print(hangman_arts.stages[lives])
        if lives == 0:
            print("You have lost all your lives, don't despair. Better luck next time!")
            break

    if "_" not in display:
        print("Congratulations!! You have {chosed_word} guessed it correctly.")
        break


    print(hangman_arts.stages[lives])
    print(display)
    