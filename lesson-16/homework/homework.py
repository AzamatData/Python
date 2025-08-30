# 1. Convert List to 1D Array
# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
# Expected Output:
# Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]
import numpy as np
my_list = [12.23, 13.32, 100, 36.32]
arr1 = np.array(my_list)
print(arr1)

# 2. Create 3x3 Matrix (2?10)
# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
# Expected Output:
# [[ 2 3 4] [ 5 6 7] [ 8 9 10]]
import numpy as np
my_3_3matrix = [[2, 3, 4], [ 5, 6, 7],[ 8, 9, 10]]
arr1 = np.array(my_3_3matrix)
print(arr1)

# 3. Null Vector (10) & Update Sixth Value
# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.
# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
import numpy as np

null_vector = np.zeros(10)
print(null_vector)
null_vector[6] = 11
print(null_vector)
# 4. Array from 12 to 38
# Write a NumPy program to create an array with values ranging from 12 to 38.
# Expected Output:
# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
import numpy as np

arr_12_38 = np.arange(12,38)
print(arr_12_38)
# 5. Convert Array to Float Type
# Write a NumPy program to convert an array to a floating type.
# Sample output:
# Original array [1, 2, 3, 4]
import numpy as np
list_data = [1, 2, 3, 4]
arr_data = np.array(list_data)
print(arr_data.dtype)
float_arr = np.asarray(arr_data, dtype=float)
print(float_arr.dtype)

# 6. Celsius to Fahrenheit Conversion
# Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.
# Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]
# Expected Output:
# Values in Fahrenheit degrees: [ 0. 12. 45.21 34. 99.91 32. ]
# Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]
# Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]
# Values in Fahrenheit degrees: [-0. 12. 45.21 34. 99.91 32. ]
import numpy as np
cvalues = [-17.78, -11.11, 7.34, 1.11, 37.73, 0]
C = np.array(cvalues)
print("Values in Centigrade degrees:")
print(C)
print("Values in  Fahrenheit degrees:")
print(np.round((9*C/5 + 32),2))

# 7. Append Values to Array (Do self-tudy)
# Write a NumPy program to append values to the end of an array.
# Expected Output:
# Original array: [10, 20, 30]
# After append values to the end of the array: [10 20 30 40 50 60 70 80 90]
import numpy as np
data = [10, 20, 30]
arr1 = np.array(data)
print(f"Original array is: \n{arr1}")

arr1 = np.append(arr1, [40, 50, 60, 70, 80, 90])
print(f"Array after append: \n{arr1}")

# 8. Array Statistical Functions (Do self-tudy)
# Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.
import numpy as np
from numpy import random
rand_arr = random.randint(100, size=10)

mean_value = np.mean(rand_arr)
median_value = np.median(rand_arr)
std_dev_value = np.std(rand_arr)

print(f"Random Array: {rand_arr}")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_dev_value}")

# 9 Find min and max
# Create a 10x10 array with random values and find the minimum and maximum values.
import numpy as np
from numpy import random
rand_arr = random.rand(10, 10)
print(rand_arr)
rand_arr_min, rand_arr_max = rand_arr.min(), rand_arr.max()

print(f"Minimum value: {rand_arr_min}\n Maximum Value: {rand_arr_max}")
# 10
# Create a 3x3x3 array with random values.

import numpy as np
from numpy import random
rand_arr = random.rand(3, 3, 3)
print(rand_arr)

