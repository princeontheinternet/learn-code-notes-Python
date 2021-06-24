
def ask_for_int():
    while True:  # if using True rem to break out of the loop

        try:
            result = int(input("Please enter a number: "))
        except:
            print("Does this looks like a number to you? Try again.")
        else:
            print(f"Great! Your number {result} is accepted")
            break
        finally:
            print("Thanks you!!!")


ask_for_int()
