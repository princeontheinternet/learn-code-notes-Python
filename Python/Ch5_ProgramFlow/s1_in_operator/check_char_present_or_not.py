# Take input from user and check whether the char is present in string "Keyboard"

text = "KeyBoard"
user_input = input("Enter a character: ")

# casefold() is a string method that converts string into lower case
if user_input.casefold() in text.casefold():
    print("{} is present in {}".format(user_input, text))
else:
    print("NO! Not Present. {} is not present in {}".format(user_input, text))


#   Output:

# Enter a character: b
# b is present in KeyBoard
