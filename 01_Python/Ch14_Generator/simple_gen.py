def get_odd():
    n = 1
    while True:
        yield n
        n += 2


odd = get_odd()

for i in range(10):
    print(next(odd))
