"""
Exception Handling:
***********************

TRY: The try block lets you test a block of code for errors.

EXCEPT: The except block lets you handle the error.

FINALLY: The finally block lets you execute code, regardless of the result of the try and except blocks.

"""

x = 10

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
finally:
    print("The 'try except' is finished")