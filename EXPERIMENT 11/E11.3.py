# WAP for NumPy array properties and functions
import numpy as np

ones_array = np.ones((2, 3))
zeros_array = np.zeros((2, 3))
empty_array = np.empty((2, 3))

print("Ones Array:\n", ones_array)
print("Zeros Array:\n", zeros_array)
print("Empty Array:\n", empty_array)

print("\nProperties of Ones Array:")
print("Shape:", ones_array.shape)
print("Data type:", ones_array.dtype)
print("Dimensions:", ones_array.ndim)
print("Size:", ones_array.size)

print("\nFunctions on Ones Array:")
print("Sum:", np.sum(ones_array))
print("Mean:", np.mean(ones_array))
print("Max:", np.max(ones_array))
print("Min:", np.min(ones_array))