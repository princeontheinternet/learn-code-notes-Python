import numpy as np

normal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(normal)

narange_way = np.arange(0, 10)
print(narange_way)

narange_with_step = np.arange(0, 11, 2)
print()


# RESIZING
narange_with_step.resize(3,2)
print(narange_with_step)

