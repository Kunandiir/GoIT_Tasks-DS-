import numpy as np

# Create two one-dimensional arrays of size 5
a = np.random.randint(1, 11, size=5)
b = np.random.randint(1, 11, size=5)

# Perform element-wise operations
addition = a + b
subtraction = a - b
multiplication = a * b

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)