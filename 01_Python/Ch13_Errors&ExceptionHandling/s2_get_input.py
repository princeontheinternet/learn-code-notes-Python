
def ask_for_int():
    while True:  # if using True rem to break out of the loop

        try:
            result = int(input("Please enter a number: "))
        except:
            print("Does this looks like a number to you? Try again.")
        else: 
            # You can use an else block after except cause in try-except statements.
            # else clause will be executed if and only if try does not raise exception.

            print(f"Great! Your number {result} is accepted")
            break
        finally:
            print("Thanks you!!!")


ask_for_int()
