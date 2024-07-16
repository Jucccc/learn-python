import numpy as np

# create array from a python list:
arr = np.array([1,2,3,4,5])

# using built-in functions:
zeros_arr = np.zeros((3,4)) # creates a 3*4 array filled with zeros
ones_arr = np.ones((2,3)) # filled with ones
random_arr = np.random.random((2,2)) # random values
arr1 = np.arange(0,10,2) # creates an array [0,2,4,6,8]
arr2 = np.linspace(0,1,5) # creates an array [0. , 0.25 , 0.5 , 0.75 , 1.]

print(arr[0])
print(arr[-1])
print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[::2])

# Reshape
arr3 = np.arange(1,10)
reshaped_arr3 = arr3.reshape((3,3))
print(reshaped_arr3)

# Concatenating arrays
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result = np.concatenate((arr1,arr2))
print(result)
result = np.hstack((arr1,arr2)) # horisontally stack
print(result)
arr1 = np.array([
    [1,2],
    [3,4]
])
arr2 = np.array([
    [5,6],
    [7,8]
])
result = np.vstack((arr1,arr2))
print(result)

# Changing array dimensions - flatten, ravel
# Flatten:
# flatten will create a new array while ravel does not create a copy
# Ravel:
# modifying the flattened (raveled) array also affects the original array if they share the same memory
# however, if the original array has a non-contiguous memory layout, ravel() creates a new array with contiguous memory

flattened_arr = arr1.flatten()
print(flattened_arr)
reshaped_arr = flattened_arr.reshape((2,2))
print(reshaped_arr)
raveled_arr = reshaped_arr.ravel()
print(reshaped_arr)
print(raveled_arr)
raveled_arr[0] = 9
print(raveled_arr)
print(reshaped_arr)

# Mathematical operations
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(arr1 + arr2) # element-wise addition
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1 ** arr2) # element-wise exponentiation