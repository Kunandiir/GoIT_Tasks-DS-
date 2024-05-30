import numpy as np

# Create two 2x2 matrices filled with random integers in the range from 1 to 10
a = np.random.randint(1, 11, size=(2, 2))
b = np.random.randint(1, 11, size=(2, 2))

# Find the product of the matrices
result = np.dot(a, b)


print(result)