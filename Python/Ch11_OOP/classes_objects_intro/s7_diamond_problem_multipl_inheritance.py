# Diamond Shape Problem in Multiple Inheritance in Python

# Multiple Inheritance and diamond problem -> https://www.geeksforgeeks.org/multiple-inheritance-in-python/
# Inheritance follows MRO Method Resolution Order

# This is also valid for method overriding.

class Class1:
    a = 1

    def feature_1(self):
        print("This is Feature 1 of class 1")


class Class2(Class1):
    a = 2

    def feature_1(self):
        print("This is Feature 1 from class 2")


class Class3(Class1):
    a = 3

    def feature_1(self):
        print("This is Feature 1 from class 3")


# Inheritance follows MRO Method Resolution Order
class Class4(Class2, Class3):
    a = 4

    def feature_1(self):
        super().feature_1()  # #########################################################
        print("This is Feature 1 from class 4")

    pass


obj1 = Class4()

print(obj1.a)
obj1.feature_1()
