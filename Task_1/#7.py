import numpy as np

# Create two matrices of size 2x2 and 2x3
a = np.random.randint(1, 11, size=(2, 2))
b = np.random.randint(1, 11, size=(2, 3))

# Multiply the matrices
result = np.dot(a, b)

print(result)