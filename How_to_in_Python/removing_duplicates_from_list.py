# Removing Duplicates in a list

def using_set(sample_list):
    return list(set(sample_list))


def using_dictionary(sample_list):
    return list(dict.fromkeys(my_list))


def using_for_loop(sample_list):
    result = []
    for i in sample_list:
        if i not in result:
            result.append(i)
    return result


def using_list_comprehension(sample_list):
    result = []
    [result.append(i) for i in sample_list if i not in result]
    return result


if __name__ == "__main__":

    my_list = ["a", "b", "a", "c", "c"]

    print(using_set(my_list))

    print(using_dictionary(my_list))

    print(using_for_loop(my_list))

    print(using_list_comprehension(my_list))

