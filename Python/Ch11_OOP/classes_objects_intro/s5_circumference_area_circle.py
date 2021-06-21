# Circumference and Area of a circle

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * Circle.pi * self.radius

    def area(self):
        return Circle.pi * self.radius * self.radius


my_circle = Circle(10)

print("The radius of my circle is {}".format(my_circle.radius))
print("Circumference of my circle is {}".format(my_circle.circumference()))
print("Area of my circle is {}".format(my_circle.area()))
