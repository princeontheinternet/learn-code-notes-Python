# 4. Methods

class Dog:
    # class object attributes
    # same for any instance
    species = 'mammal'  # CLASS/STATIC VARIABLE ---> self keyword not required

    def __init__(self, breed, name, spot):
        self.breed = breed
        self.name = name
        # Expecting a boolean
        self.spot = spot

    # Operation/Actions
    def bark(self, number):
        print(" WOOF! My name is {} and the number is {}".format(self.name, number))     # self.name and not name bcz name is now self.name


# creating a object
my_dog = Dog('Lab', 'Huskey', False)    # positional arguments

print(my_dog.breed)  # Lab
print(my_dog.species)  # mammal

# for methods you have to put parenthesis and for var not required.
my_dog.bark(10)
