

class Computer:

    def config(self):
        print("i5, 16GB, 1TB")


com1 = Computer()   # object creation
com2 = Computer()

print(type(com1))

# This is what happens, self is the object you are calling
Computer.config(com1)
Computer.config(com1)

# We use this
com1.config()
com2.config()