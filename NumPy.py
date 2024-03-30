import numpy as np

arr = np.array([10,20,30,56,67,76,5,65])
arr1 = np.array([[10,20,30],[23,34,43],[45,54,32]])

print(np.shape(arr1))  # Prints the shape of arr1
print(arr[:7])  # Prints the first 7 elements of arr using array slicing
print(np.size(arr))  # Prints the size of arr (total number of elements)
print(np.random.randint(1, 101))  # Prints a random integer between 1 and 100


import numpy as np
a = ([[30,40,50],[32,65,90]])
arr = np.array(a)
print(arr)
print(arr.shape) #rows, columns
print(len(arr)) #number of nested values
print(np.size(arr)) #number of elements
print(type(arr)) #datatype of variable
print(arr.dtype) #dataype of array
print(arr.astype(int)) #conversion of datatype

import numpy as np
arr = ([13,32,22,34,44,43,33])
print(arr)
print(np.add(arr,2))
print(np.subtract(arr,2))
print(np.multiply(arr,2))
print(np.divide(arr,2))
print(np.power(arr,2))
print(np.sqrt(arr))

# combining and splitting arrays
import numpy as np

arr = np.array([[12,23],[34,45],[56,67],[78,89]])
arr1 = np.array([[21,32],[43,54],[65,76],[87,98]])

# print(np.concatenate([arr,arr1]))
print(np.hstack([arr,arr1]))
print()
print(np.vstack([arr,arr1]))

# splitting array
import numpy as np

arr = np.array([12,23,34,45,56,67,78,89])
arr1 = np.array([[21,32],[43,54],[65,76],[87,98]])

p = np.array_split(arr,4)
q = np.array_split(arr1,2)
print(p)
print(q)
print(p[2])

# adding, inserting, deleting
import numpy as np

arr = np.array([12,23,34,45,56,67,78,89])
arr1 = np.array([[21,32],[43,54],[65,76],[87,98]])

arr = np.append(arr,46)
arr1 = np.append(arr1,46)

print(arr)
print(arr1)

arr = np.insert(arr,3,44)
print(arr)

arr = np.delete(arr,3)
print(arr)

# sort, filter, search
import numpy as np

arr = np.array([12,21,34,43,22,76,67,88,76])
arr1 = np.array([[21,32,43,54],[95,56,87,98]])
print(np.sort(arr))
# print(np.sort(arr1))

p = np.where(arr % 2 == 0)
print(p)

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(1, 3, 4)

print(newarr)

import numpy as np
arr=([12,21,22,33,34,43,36,65,56,77])
arr = np.sort(arr)

ans = np.searchsorted(arr,36)
print(arr,ans)

# Agregate functions in NumPy
import numpy as npm

arr = npm.array([9,1,2,4])
print("Sum:",np.sum(arr))
print("Minimum:",np.min(arr))
print("Maximum:",np.max(arr))
print("Number of elements:",np.size(arr))
print("Mean:",np.mean(arr))
print("Cummutative Sum:",np.cumsum(arr))
print("Cummutative Product:",np.cumprod(arr))

a = [100,150,199,200,250,130]
b = [10, 50, 30, 40, 30, 10]

price = np.array(a)
quantity = np.array(b)
print ( price,"\n",quantity)

c = np.cumprod([price,quantity],axis = 0)
print("Quantity:",c[0])
print("Price:",c[1])
print("Total:",c[1].sum())

# statistical functions
import numpy as np
import statistics as stats
a = [150,100,110,145,120,140,130,105]

arr = np.array(a)
print("Mean:",np.mean(arr))
print("Median:",np.median(arr))
print("Mode:",stats.mode(arr))
print("Standard Deviation:",np.std(arr))
print("Varience:",np.var(arr))
