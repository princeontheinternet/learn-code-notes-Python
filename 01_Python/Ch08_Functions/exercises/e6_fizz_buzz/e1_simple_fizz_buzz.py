# your fizz_buzz function should return the correct word("fizz", "buzz" or "fizz_buzz")
# or the number if it is not divisible by 3 or 5.


def fizz_buzz(number: int) -> str:
    """
    Play Fizz buzz

    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if (number % 3 == 0) and (number % 5 == 0):
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


for i in range(1, 101):
    print(fizz_buzz(i))
