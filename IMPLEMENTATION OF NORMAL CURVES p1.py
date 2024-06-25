import numpy as np 
import matplotlib.pyplot as plt 
x = np.linspace(1,50,200) 
#Creating a Function. 
def normal_dist(x , mean , sd): 
 prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2) 
 return prob_density 
mean = np.mean(x) 
sd = np.std(x) 
#Apply function to the data. 
pdf = normal_dist(x,mean,sd) 
 #Plotting the Results 
plt.plot(x,pdf , color = 'red') 
plt.xlabel('Data points') 
plt.ylabel('Probability Density')
plt.show()