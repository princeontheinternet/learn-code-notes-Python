# WAP to print fibonacci series:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fibonacci_series(n: int) -> int:
    """
    Returns the fibonacci result

    :param n: `n` is the user input.
    :return: It will return `n` if value is between 0 & 1 inclusively else it will return `result` of fibonacci series.
    """
    if 0 <= n <= 1:
        return n  # if no is 0 or 1

    result = 0
    i, j = 0, 1
    for loop in range(n - 1):
        result = i + j
        i = j  # swapping j to i
        j = result  # swapping result to j
    return result


user_input = int(input("Enter number till which u want fibonacci series: "))
for val in range(user_input):
    print(val, fibonacci_series(val))
