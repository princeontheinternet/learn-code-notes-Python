# 2. self.attribute_name concept.

class Dog:

    def __init__(self, breed):
        self.my_breed = breed  # self.attribute gives attribute a name. Attribute means characteristics/var of class.


my_dog = Dog(breed='Lab')

print(my_dog.my_breed)
