#Histogram Example 
import matplotlib.pyplot as plt 
import numpy as np 
# Creating dataset 
a = np.array([61, 63, 64, 66, 68, 69, 69.5, 70, 72, 
72.5, 73, 73.5, 74, 74.5, 76, 76.2, 
76.5, 77, 77.5, 78, 78.5, 79, 79.2, 
80, 81, 82, 83, 84, 85, 87]) 
# Creating histogram 
fig, ax = plt.subplots(figsize =(10, 7)) 
ax.hist(a, bins = [60,65,70,75,80,85,90]) 
# Show plot 
plt.show() 