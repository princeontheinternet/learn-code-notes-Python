"""
WHAT IS NUMPY?

    1. NumPy is a Python library used for working with arrays.
    2. It also has functions for working in domain of linear algebra, fourier transform, and matrices.
    3. NumPy was created in 2005 by Travis Oliphant.
       It is an open source project and you can use it freely.
    4. NumPy stands for Numerical Python.

WHAT IS ARRAY AND HOW IT IS FASTER THAN LIST?

    1. NumPy arrays are stored at one continuous place in memory unlike lists,
    so processes can access and manipulate them very efficiently.

"""

import numpy as np

arr = np.array([1, 2, 3, 4])  # [1 2 3 4]
print(arr)

# The array object in NumPy is called ndarray.
print(type(arr))  # <class 'numpy.ndarray'>
