# Inheritance:

# Code Re-usability.

# Base Class
class Animal:

    def __init__(self):
        print('Animal Created')

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


# Derived Class
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    # overriding who_am_i
    def who_am_i(self):
        print("I am a dog")


my_animal = Animal()
my_dog = Dog()

my_animal.who_am_i()
my_dog.who_am_i()

my_animal.eat()
my_dog.eat()


