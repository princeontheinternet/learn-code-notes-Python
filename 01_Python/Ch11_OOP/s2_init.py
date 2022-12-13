

class Computer:

    def __init__(self, cpu, ram): # init is just like constructor
        # print("This is init. It gets called every time an object is created.")
        pass

    def config(self):
        print("i5, 16GB, 1TB")


com1 = Computer('i5', 16)   # object creation
com2 = Computer('i5', 16)

# com1.config()
# com2.config()