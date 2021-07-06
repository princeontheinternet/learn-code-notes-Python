# Fibonacci series

def normal_fibon(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def gen_fibon(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


# This will occupy space
print(normal_fibon(10))

# This will not occupy space but to access it you will have to apply loop
# print(gen_fibon(10))    # <generator object gen_fibon at 0x000001A405139580>

for number in gen_fibon(10):
    print(number)

# Next() in generator
g = gen_fibon(10)
# print(next(g))  # 0
# print(next(g))  # 1

s = "hello"
s = iter(s)
print(next(s))
