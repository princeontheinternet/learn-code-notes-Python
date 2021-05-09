low = int(input("Enter the lowest number for the range: "))
high = int(input("Enter the highest number for the range: "))

print("Please think of a number between {} and {}".format(low, high))
input("Press Enter to start the game!!!")

no_of_attempt = 1

while low != high:

    #    print("\tGuessing in the range of {} to {}".format(low, high))

    guess = low + (high - low) // 2
    high_low = input("My guess is {}. "
                     "Press h for higher, l for lower and c for correct: ".format(guess)).casefold()

    if high_low == 'h':
        low = guess + 1

    elif high_low == 'l':
        high = guess - 1

    elif high_low == 'c':
        print("I got it in {} attempt.".format(no_of_attempt))
        break

    else:
        print("Please enter h, l or c.")

    no_of_attempt += 1

    if high == low:
        print("I found on my own. Your number is {}. I found it in {} attempt.".format(low, no_of_attempt))


