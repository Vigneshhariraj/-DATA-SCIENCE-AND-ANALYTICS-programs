import numpy as np 
dicti = {'a': 20, 'b': 32, 'c': 12, 'd': 93, 'e': 84} # creating our test dictionary 
listr = [] 
for value in dicti.values(): 
 listr.append(value) 
mean=np.mean(listr) 
std = np.std(listr) 
print(mean) 
print(std) 