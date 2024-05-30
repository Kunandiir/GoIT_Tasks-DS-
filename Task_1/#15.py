import numpy as np

# Create two 4x4 matrices filled with random integers in the range from 1 to 10
a = np.random.randint(1, 11, size=(4, 4))
b = np.random.randint(1, 11, size=(4, 4))

# Find the difference of the matrices
result = a - b


print(result)