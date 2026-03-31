#WAP FOR SAVING AND LOADING ARRAYS
import numpy as np
arr = np.array([1, 2, 3, 4])

np.save('my_array.npy', arr)
print("Array saved successfully!")

loaded_arr = np.load('my_array.npy')
print("Loaded Array:", loaded_arr)