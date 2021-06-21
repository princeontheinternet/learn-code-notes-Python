# Classes and Objets


"""
Classes and Objects:

Class: blueprint for creating objects. Written in PascalCase.

1. Class Name
2. Class object attributes - variables - which will be same for all the instances
3. __init__() method
4. Normal method
objects: Instance of a Class.


Attributes: Variables/characteristics of a Class.


__init__():

1. All classes have a function called __init__(), which is always executed when the class is being initiated.
2. It is used to assign values to object properties, that are necessary to do when the object is being created.
3. The __init__() function is called automatically every time the class is being used to create a new object.


self.attribute_name:    # ref to instance of a class

1. The self parameter is a reference to the current instance of the class,
   and is used to access variables that belongs to the class.
2. it has to be the first parameter of any function in the class.


"""


# 1. Basics of creating class and object

class Dog:

    def __init__(self, breed):
        self.breed = breed


my_dog = Dog(breed='Lab')     # Creating object

print(type(my_dog))  # <class '__main__.Dog'>