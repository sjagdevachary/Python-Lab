#Wap for ndarray of object, indexing, and slicing.
import numpy as np
arr= np.array([[1,2,3],[4,5,6]])
print("Array:\n",arr)
arr=np.array([[10,20,30],[40,50,60]])
print("Element at(0,1):",arr[0,1])#indexing
print("Row1:",arr[1,:])
print("Column2:,arr[:,2]")
