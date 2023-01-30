# Importing Modules

"""
MODULE: A file containing a set of functions you want to include in your application.
        You can call it as another Python file which contains functions.
        
There are 2 types of modules:
1. Built in Modules: Pre installed with Python. Eg: hashlib, csv, etc
2. External Modules: Need to install using pip. Eg: Pandas, Tensorflow, etc

IMPORT: The import keyword is used to import modules.

FROM: The from keyword is used to import only a specified section from a module.

from module import *: import * means importing all the functions from the module.

AS: As keyowrd is used to give alias to a module

dir: dir function can be used to view the names of all the function and variables defined in a module.

"""

import math
print(math.pi)

# Using As keyword to give alias
import math as m
print(m.pi)

# Using from keyword to import only specified section from module
from math import pi
print(pi)

from math import *      
print(pi)
# Not recommended as it will import everything, 
# there may be a possibility of same var/fn name in the current prgm & imported module,
# and it may lead to confusion.

import math
print(dir(math))


import turtle
turtle.forward(150)
turtle.right(90)
turtle.circle(80)
turtle.done()