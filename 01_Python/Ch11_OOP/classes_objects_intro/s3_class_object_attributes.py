# 3. Class object attributes - same for any/all instance

class Dog:

    # class object attributes
    # same for any instance
    species = 'mammal'  # self keyword not required

    def __init__(self, breed, name, spot):
        self.breed = breed
        self.name = name
        # Expecting a boolean
        self.spot = spot


# creating a object
my_dog = Dog(breed='Lab', name='Huskey', spot=False)

print(my_dog.breed)  # Lab
print(my_dog.species)  # mammal
