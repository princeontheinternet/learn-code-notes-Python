# WAP to create a fizzbuzz program using list comprehension


list_comprehension = [
    "fizbuzz" if (i % 3 == 0) and (i % 5 == 0) else "fizz" if (i % 3 == 0) else "buzz" if (i % 5 == 0) else str(i)
    for i in range(1, 16)]

print(list_comprehension)
