# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs

def get_int_value():
    while True:
        try:
            n = int(input("Enter a number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            break

    print(f"The square of the number {n} is {n**2}")


get_int_value()

