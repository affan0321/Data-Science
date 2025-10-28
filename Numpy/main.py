import numpy as np

# arr = np.arange(1,31).reshape(6,5)
# print(arr)

# print(arr[0:2,1:3])

# slice = arr[3:,3:]
# print(slice)



# arr = np.arange(11,21)
# print(arr)
# bool_index= arr%2 ==0
# print(bool_index)

# arr = arr[bool_index]
# print(arr)


#Arithmetic operations

# a1 = np.array([1,2,3,4,5,])
# a2 = np.array([6,7,8,9,10])

# a3 = a1 + a2

# print(a3)


# Shallow copy

# arr = np.arange(1,21)
# print(arr)
# slice = arr[:4]
# print(slice *10)


# Matrix operation

# A = np.array([[1,2],[3,4]])
# B = np.array([[5,6],[7,8]])

# C = A @ B

# print(C)



# Array Excercise

# s = np.array([
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
    
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
    
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ])

# b = np.sum(s,axis=1)

# for i in b:
#     if i != 45:
#         print("Sudoku is not valid!")
#         break
#     else:
#         print("Sudoku is valid!")

# d = np.sum(s[:3,:3])


# for i in range(0,9,3):
#     for j in range(0,9,3):
#         n = s[0:3,0:3]
#         print(n.sum())



# Columns: [Age, Math Marks, Science Marks]
# data = np.array([
#     [18, 85, 78],   # Student 1
#     [19, 92, 88],   # Student 2
#     [17, 76, 95],   # Student 3
#     [18, 65, 70],   # Student 4
#     [20, 90, 85]    # Student 5
# ])


# Get the shape of matrix

# data = data.shape
# print(data)


# Average age of students

# avg = np.mean(data[:,0])
# print(avg)

# math = data[:,1]
# print(math)

# max_sci_mark = np.max(data[:,2])
# print(max_sci_mark)



# Great90 = data[data[:,1]>90]
# print(Great90)



# plus5 = data[:,1] + 5
# print(plus5)

# age = len(data[data[:,0] < 19])
# print(age)



# marksmean = np.mean(data[:,1:],axis=0)
# print(marksmean) 

# more80 = data[(data[:,1]>= 80) & (data[:,2] >= 80)]
# print(more80)






# Level 1 Questions of numpy


# Create a 3×3 identity matrix using NumPy.

# matrix = np.eye(3)
# print(matrix)

# Generate an array of 10 random integers between 1 and 100

# arr = np.random.randint(1,100,size=10)
# print(arr)

# Create a 5×5 matrix with values 1, 2, 3, 4 just below the diagonal.

# matrix = np.diag([1,2,3,4],k = -1)
# print(matrix)

# Reverse an array (first element becomes last).

# arr = np.array([1,2,3,4])
# reversed_array = arr[::-1]
# print(reversed_array)

# Create a 10×10 array and find the maximum and minimum values.

# matrix = np.random.random((10,10))
# print(matrix.max())
# print(matrix.min())

# Reshape a 1D array of 25 elements into a 5×5 matrix.

# arr = np.arange(25)
# matrix = arr.reshape(5,5)
# print(matrix)


# Extract the 2nd row and 3rd column from a 5×5 matrix.

# arr = np.arange(25)
# matrix = arr.reshape(5,5)
# slice = matrix[1:]
# slice1 = matrix[:2]
# print(slice)
# print(slice1)


# Replace all even numbers in an array with -1

# arr = np.arange(10)
# arr[arr % 2 == 0] = -1
# print(arr)




# Level 2 Questions of numpy

# Create two random 3×3 matrices and compute:

# arr = np.random.random(9)

# matrix = arr.reshape(3,3)

# arr1 = np.random.random(9)
# matrix1 = arr1.reshape(3,3)

# sum of 3x3 matrix

# for i in range(3):
#     for j in range(3):
#         result = matrix[i,j] + matrix1[i,j]
#         print(result)

# dot product of 3x3 matrix

# dot = np.dot(matrix,matrix1)
# print(dot)

# dot = matrix @ matrix1

# print(dot)



# Normalize a random 5×5 matrix (scale all values between 0 and 1).

# matrix = np.random.randint(low=0, high=100, size=(5, 5))
# print(matrix)

# minValue = matrix.min()
# maxValue = matrix.max()

# normalized = (matrix - minValue) / (maxValue - minValue)
# print(normalized)


# Compute mean, median, variance, and standard deviation of an array.

# arr = np.arange(10)

# meanVal = np.mean(arr)
# medianVal = np.median(arr)
# varianceVal = np.var(arr)
# stdVal = np.std(arr)
# print(arr)
# print(meanVal)
# print(medianVal)
# print(varianceVal)
# print(stdVal)

