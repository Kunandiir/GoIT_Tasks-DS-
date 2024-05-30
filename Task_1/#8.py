import numpy as np


# Create a 3x3 matrix filled with random integers in the range from 1 to 10
a = np.random.randint(1, 11, size=(3, 3))

# Find the inverse of the matrix
inverse = np.linalg.inv(a)

print(inverse)