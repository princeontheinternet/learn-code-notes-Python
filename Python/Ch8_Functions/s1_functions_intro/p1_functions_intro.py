# Intro to Functions

"""
Functions:
    1. A function is a block of code which only runs when it is called.
    2. Re-usability is the main achievement of Python functions.
    3. You can pass data, known as parameters, into a function.

            :parameter : Parameters are like placeholders for the real values that you'll pass to your function.
                       : They are just variable but, they're given a value when you call the function.
                       : They are also referred as `formal parameter`

            :argument : Arguments are the values that will be used by parameters, when we call a function.
                      : Each parameter must be given a value by providing argument in the function call.
                      : Providing values as argument is called passing the arguments.

    4. A function can return data as a result using return keyword.

            :return : To return a value, use a return keyword to specify the value that should be returned.
                    : If you don't explicitly return a value, Python will automatically return None.

    5. Functions are separated by each other with 2 blank lines.

    6. There are 2 types of functions:
        1. User-defined functions: These are those functions which are defined by the user.
        2. Built-In functions: These are those functions that are provided by the python i.e. pre-defined e.g. range(), print().

Eg: def multiply(parameters):
    1. def: Function definition starts with the keyword def.
    2. multiply: Name of the function
    3. parameters: parameters are written in parentheses.
"""


def multiply(x, y):
    result = x * y
    return result


answer = multiply(10.1, 5)
print(answer)

another_answer = multiply(25, 5)
print(another_answer)

print()

for val in range(1, 11):
    two_table = multiply(2, val)
    print(two_table)

# Debug your code use (step into my code button & step out button).
#   When the function terminates, execution resumes at the point after the function call.
