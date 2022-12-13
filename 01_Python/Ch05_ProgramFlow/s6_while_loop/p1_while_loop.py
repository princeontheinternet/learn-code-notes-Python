#                   Section 6: While loop

# While loop continues to loop, as long as the condition evaluates to True, when the condition evaluated to False,
# the loop terminates and execution continues with the code after the loop

# while loop is used when you can't determine, in advance, how many times you will need to loop
#                           vs
# in for-loop you know the end value or how many times the loop will run.

# while loop is also used with else statement. Check p3_adventure_exit_game.


# for i in range(10):
#     print(i)

i = 0  # initialize a var to be used in while_loop
while i < 10:  # condition
    print("i is now {}".format(i))
    i += 1  # Augmented Assignment (increment by 1 (+=1))
    # i = i + 1

#   Output:

# i is now 0
# i is now 1
# i is now 2
# i is now 3
# i is now 4
# i is now 5
# i is now 6
# i is now 7
# i is now 8
# i is now 9
