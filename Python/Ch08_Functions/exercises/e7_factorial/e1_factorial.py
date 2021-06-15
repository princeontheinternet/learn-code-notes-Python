def factorial(n: int) -> int:
    """
    Return the factorial of nth no

    :param n: The no for which the user want factorial
    :return: Returns the factorial of nth no
    """
    if n == 0:
        return 1
    else:
        result = 1
        for number in range(n):
            result = result * (number+1)
        return result


user_input = int(input("Enter no whose factorial you want to know: "))
print("{}! = {}".format(user_input, factorial(user_input)))
