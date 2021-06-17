# *args is arguments that returns tuples
# **kwargs is the keyword argument that returns a dictionary.

def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print("I did not find any fruit")


myfunc(fruit='apple', veggie='lettuce')