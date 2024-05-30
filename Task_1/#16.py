import numpy as np


# Create a 3x3 matrix filled with random floating-point numbers in the range from 0 to 1
a = np.random.rand(3, 3)

# Find the vector of row sums
row_sums = np.sum(a, axis=1)

print(row_sums)