"""
    So when the interpreter runs a module, the __name__ variable will be set as  __main__
    if the module that is being run is the main program.

    But if the code is importing the module from another module,
    then the __name__  variable will be set to that module’s name.


"""

print("First Module's Name: {}".format(__name__))


def my_func():
    print("This is my function in module: {}".format(__name__))


if __name__ == "__main__":
    my_func()
    print("\n This is useless piece of line.")
    print("If this is not put under __main__ then it will be executed in another module.")

# The above two print function will not get executed
