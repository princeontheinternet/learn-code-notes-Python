import s1


def s2_my_func():
    print("This is my function in: {}".format(__name__))


if __name__ == "__main__":
    print("Second module name: {}".format(__name__))
    s1.my_func()
    s2_my_func()
