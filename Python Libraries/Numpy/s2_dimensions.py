import numpy as np

# 0-D
print(np.array(42))

# 1-D
# array that has 0-D arrays as its elements.
print(np.array([1, 2, 3, 4, 5, 6]))

# 2-D
# array that has 1-D arrays as its elements.
print(np.array([[1, 2, 3], [4, 5, 6]]))
# observe the no. of square brackets


# 3-D
# array that has 2-D arrays (matrices) as its elements.
print(np.array([[[1, 2, 3], [4, 5, 6]]
                   , [[1, 2, 3], [4, 5, 6]]]))
