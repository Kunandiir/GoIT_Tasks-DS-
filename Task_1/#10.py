import numpy as np


# Create a 3x4 matrix and a 4-element vector filled with random integers in the range from 1 to 10
a = np.random.randint(1, 11, size=(3, 4))
b = np.random.randint(1, 11, size=4)

# Multiply the matrix by the vector
result = np.dot(a, b)

print(result)