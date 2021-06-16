# Basics Of I/O with files using "with" statement


# The below piece of code rewrites and creates a file if it doesn't exist.
with open('test.txt', 'w') as my_file:
    my_file.write("This is a new file which I created using write method.\nI will append to this file later")


# This will read and print the lines of the file in the o/p
with open('test.txt', 'r') as my_file:
    print(my_file.read())


# This will create a list, which will contain each line as an element. This is the functionality of readlines() method.
with open('test.txt', 'r') as my_file:
    print(my_file.readlines())

