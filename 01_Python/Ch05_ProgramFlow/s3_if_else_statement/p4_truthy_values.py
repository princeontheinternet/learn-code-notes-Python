# 0, False, Empty string, all means False.

if 0:
    print("True")
else:
    print("False")

name = input("Please Enter your name: ")

if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you a man with no name?")
