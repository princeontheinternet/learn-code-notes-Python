#                       Section 7: TypeCasting

# The conversion of one data type into the other data type is known as type casting in python.

# Eg:  int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc.

# Two Types of Typecasting:
# 1. Explicit Conversion: When developer does it.
# 2. Implicit Conversion: When Python does it internally

# Explicit Conversion:

a = "2"
b = 3

converted_a = int(a)   #throws an error if the string is not a valid integer

print(f"The sum of {converted_a} + {b} is {converted_a+b}")



# Implicit Conversion:

# Some of the data types have higher-order(precedence), and some have lower order.

# While performing any operations on variables with different data types in Python, 
# one of the variable's data types will be changed to the higher data type by Python interpreter itself.

a = 3.8 # float
b = 2   # int

print(a+b)  # 5.8 which is float and not int.



