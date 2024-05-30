import numpy as np

# Create a 5x5 matrix filled with random integers in the range from 1 to 100
a = np.random.randint(1, 101, size=(5, 5))

# Find the sum of the elements
sum_elements = np.sum(a)

print(sum_elements)