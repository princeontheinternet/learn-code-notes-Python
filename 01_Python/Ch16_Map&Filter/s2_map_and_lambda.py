def square(num):
    return num ** 2


print(square(5))  # 25

list1 = [2, 3, 4, 5, 6, 7]

print(map(square, list1))  # <map object at 0x00000206CFCF8BB0>
print(list(map(square, list1)))  # [4, 9, 16, 25, 36, 49]


# Map and lambda

print(list(map(lambda num: num ** 2, list1)))   # [4, 9, 16, 25, 36, 49]


