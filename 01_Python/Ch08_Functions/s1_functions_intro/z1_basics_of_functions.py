# Return True even if a single number in the list is true, otherwise False

def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            # return False  # it will return false even if a single number is odd and others are evn. Wrong logic.
            pass

    return False  # After completion of loop it will return False if no number is found even.


def return_even_list(num_list):
    even_list = []
    for number in num_list:
        if number % 2 == 0:
            even_list.append(number)

    return even_list


print(check_even_list([1, 3, 5]))
print(check_even_list([2, 1, 1]))
print(check_even_list([1, 3, 2]))

print("*" * 90)


print(return_even_list([1, 1, 1]))
print(return_even_list([1, 3, 2]))
print(return_even_list([4, 3, 2]))