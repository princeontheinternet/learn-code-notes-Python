# sum of numbers using var-positional argument.

def sum_numbers_regular_method(*values: float) -> float:
    result = 0
    for number in values:
        result += number
    return result


def sum_numbers_built_in(*values: float) -> float:
    return sum(values)


print(sum_numbers_regular_method(1, 2, 3))
print(sum_numbers_built_in(1, 2, 3))
