def even_odd(*args, k):
    if k == 'e':
        even_list = [values for values in args if values % 2 == 0]
        return even_list
    elif k == 'o':
        odd_list = [values for values in args if values % 2 != 0]
        return odd_list


even = even_odd(1, 2, 3, 4, k='e')
odd = even_odd(1, 2, 3, 4, 5, 6, 7, k='o')
print(even)
print(odd)