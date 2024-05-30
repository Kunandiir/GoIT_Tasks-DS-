import numpy as np


# Create a 2x3 matrix and a 3-element vector filled with random floating-point numbers in the range from 0 to 1
a = np.random.rand(2, 3)
b = np.random.rand(3)

# Multiply the matrix by the vector
result = np.dot(a, b)

print(result)