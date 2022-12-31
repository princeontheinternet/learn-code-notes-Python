
# No need to close the file using with
with open("sample.txt", 'r') as v2:
    for line in v2:
        print(line, end="")

# Without using with if there was an error in reading the file, the program may stop and the file may not be closed.
# This could cause problem or corrupt a file.

# but with "with" statement it will take care of closing the file even if there's an error in reading a file.

