#wap for data types and structures in Numpy
import numpy as np

arr = np.array([1, 2, 3])
print("Data type:", arr.dtype)

arr = arr.astype('float64')   # corrected here
print("Updated type:", arr.dtype)