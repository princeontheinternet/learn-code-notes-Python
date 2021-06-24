# Operator Overloading:
# Taking + and using it in different ways like + for int will add numbers and + for string will concatenate strings.

# Method Overloading:
# Method Over loading is when two methods have same name and different parameters.
# Python doesn't support method over loading.
# We may overload the method but Python will only consider the latest method.
# https://www.geeksforgeeks.org/python-method-overloading/


# Operator Overloading
"""
When we add 5+6, behind the scenes int.__add__(a,b) gets executed.
So if if your class you want to add then you will have to overload the add method.
"""
# Example
a = 8
b = 9
c = int.__add__(a, b)
print(c)


class Student:

    def __init__(self, name, m1, m2):
        self.name = name
        self.m1 = m1
        self.m2 = m2

    def __str__(self):
        return f"{self.name}'s Marks: \nM1: {self.m1} \nM2: {self.m2}"

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False


s1 = Student('Ram', 90, 95)
s2 = Student('Laxman', 55, 70)

print(s1)  # <__main__.Student object at 0x000001D84B62D3D0>
# We have to do operator overload of __Str__

print(s2)

if s1 > s2:
    print(f"{s1.name} has more marks than {s2.name}")
else:
    print(f"{s2.name} has more marks than {s1.name}")


