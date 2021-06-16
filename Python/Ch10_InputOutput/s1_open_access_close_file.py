
# 1. Opening a file
# The open() function takes two parameters; filename, and mode.
v1 = open("sample.txt", 'r')


# 2. Accessing a file
# The open() function returns a file object, which has a read() method for reading the content of the file
print(v1.read())

v1.readlines()  # returns each line as an element of a list

# Loop through the file line by line:
# for i in v1:
#     print(i, end="")

# for i in v1:
#     if "Twas" in i:
#         print(i, end="")


# 3. Closing a file
# Closing a file is imp as if not closed, the file may get corrupted.
v1.close()


