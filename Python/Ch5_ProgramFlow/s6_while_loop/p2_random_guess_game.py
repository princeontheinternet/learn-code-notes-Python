import random
"""
What is a module?
    1. A module is a file containing Python definitions and statements.
    2. The file name is the module name with the suffix .py appended.
    3. Each .py you create becomes a new python module. 
    4. Modules can be imported into another modules, or executed.
"""

lowest = int(input("Please Enter the lowest no for the range you want to guess: "))
highest = int(input("Please Enter the Highest no for the range you want to guess: "))

answer = random.randint(lowest, highest)
# randint function is present in the random module and produces random integer within the range.

# print("The secret answer is {}".format(answer)) # TODO: Remove after testing

print("\nLets start the Game!!!!!\n")

guess = int(input("Guess a no between {} and {}: ".format(lowest, highest)))

no_of_attempt = 1

if guess == answer:
    print("You got it in 1st attempt")
else:
    while guess != answer:
        if guess == 0:
            break
        elif guess < answer:
            print("Please guess higher OR Press 0 for exit")
        elif guess > answer:
            print("Please guess lower OR Press 0 for exit")
        guess = int(input())
        no_of_attempt += 1  # Augmented Assignment (increment by 1 (+=1))
        # no_of_attempt = no_of_attempt + 1

        if guess == answer:
            print("Bingo!!! You got the answer in {} attempt".format(no_of_attempt))

