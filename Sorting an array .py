import numpy as np 
a = np.array([[1, 4, 2], [3, 4, 6], [0, -1, 5]])  
print("Array before sorting")  
print(np.sort(a, axis=None))  
print("Sorting in row wise :")  
print(np.sort(a, axis=1)) 
print("Sorting in column wise :") 
print(np.sort(a, axis=0))