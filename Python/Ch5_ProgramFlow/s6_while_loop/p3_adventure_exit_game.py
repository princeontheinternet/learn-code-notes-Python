available_exit = ["north", "south", "east", "west"]
chosen_exit = ""

# casefold() is a string method that converts string into lower case
# strip() is a string method that returns a trimmed version of the string. Removing spaces.

while chosen_exit.casefold().strip() not in available_exit:
    chosen_exit = input("Please enter a direction to get out of this game! OR press q to exit: ")
    if chosen_exit.casefold() == "q":
        print("Game Over! You die!!!")
        break  # bcz of break else loop will not get executed
        # and the while loop with else loop will break.
else:
    print("You are away as your exit, which is {}, "
          "was one of the exit in {}".format(chosen_exit, available_exit))

#   Output:

# Please enter a direction to get out of this game! OR press q to exit: up
# Please enter a direction to get out of this game! OR press q to exit: down
# Please enter a direction to get out of this game! OR press q to exit: west
# You are away as your exit, which is west, was one of the exit in ['north', 'south', 'east', 'west']
