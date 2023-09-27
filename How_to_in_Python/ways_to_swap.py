# Ways to swap number

def swap1(x: int, y: int) -> None:
    # 1. Using Temporary Variable Approach

    temp = x
    x = y
    y = temp

    print("Value of 1st number is {}".format(x))
    print("Value of 2nd number is {}".format(y))


def swap2(x: int, y: int) -> None:
    # 2. Using Tuple/List

    (x, y) = (y, x)
    # [x,y] = [y,x]

    print("Value of 1st number is {}".format(x))
    print("Value of 2nd number is {}".format(y))


def swap3(x: int, y: int) -> None:
    # 3. Using Arithmetic Operators
    
    x = x + y
    y = x - y
    x = x - y

    print("Value of 1st number is {}".format(x))
    print("Value of 2nd number is {}".format(y))


a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
swap3(a, b)

