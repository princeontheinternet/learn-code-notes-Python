# WAP to check string is palindrome or not.

"""
    Palindrome: It is a word that reads the same backwards as forwards.
            Word Eg: Radar, Ma'am, Civic.
        Sentence Eg: Was it a car, or a cat, I saw?
"""


def is_palindrome(string):
    """
    It will check for a Palindrome by comparing reversed string with original and
    return `True` or `False` based on that.

    :param string: The string entered by the user.
    :return: It will return either True or False after checking for a palindrome.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()   # Previous 2 lines converted into single line.
# Advantage of function: When you fix the function all the code that calls it gets the advantage of the fix.


def palindrome_sentence(sentence):
    """

    :param sentence:
    :return:
    """

    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    print(string)   # TODO: remove after testing

    return is_palindrome(string)
# calling another function.


word = input("Please enter a word to check: ")

if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
