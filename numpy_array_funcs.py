import numpy as np

arr1 = np.array([1, 2, 3])
# print("Numpy Array : " , arr1)
zeros_arr = np.zeros((2, 3)) #Create an array of zeros with a specified shape.(rows , cols)
# print("Zeros Array : " , zeros_arr)

ones_arr = np.ones((2, 3)) #Create an array of ones with a specified shape. (rows , cols)
# print("Ones Array : " , ones_arr)
range_arr = np.arange(0, 10, 2) # Create an array with regularly spaced values. (start , end , steps)
# print("Regularly shaped values : " , range_arr)

linspace_arr = np.linspace(0, 2, 5) # Create an array with evenly spaced values over a specified range.
# print("Evenly Spaced Values : " , linspace_arr)

identity_mat = np.eye(3) #  Create an identity matrix.
# print("Identity matrix : " , identity_mat)

# Array Operations
arr = np.array([[1, 2, 3], [4, 5, 6] , [7, 8, 9]])
shape = np.shape(arr)
print(arr)
print("Shape of Array = " , shape)
s = range_arr.sum()
print("Sum of Array : ", s)
'''reshaped_arr = np.reshape(arr, (5,2))
print()
print(reshaped_arr)'''

arr2 = np.array([4, 25, 36, 49, 625])
sqrt_arr = np.sqrt(arr2)
exp_arr = np.exp(arr2)
print("Sqrt of int Array Elements = " , sqrt_arr)
print("Exp of int Array Elements = " , exp_arr)


