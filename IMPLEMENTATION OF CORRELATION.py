import numpy as np 
import scipy.stats as stats 
import matplotlib.pyplot as plt 
import pandas as pd 
experience = [1, 3, 4, 5, 5, 6, 7, 10, 11, 12, 15, 20, 25, 28, 30,35] 
salary = [20000, 30000, 40000, 45000, 55000, 60000, 80000, 100000, 130000, 150000, 
 200000, 230000, 250000, 300000, 350000, 400000] 
data = {'expr':[1, 3, 4, 5, 5, 6, 7, 10, 11, 12, 15, 20, 25, 28, 30,35], 
 'sal':[20000, 30000, 40000, 45000, 55000, 60000, 80000, 100000, 130000, 150000, 
 200000, 230000, 250000, 300000, 350000, 400000], 
 'age':[20,30,36,40,28,40,50,54,49,47,45,39,29,40,30,38]} 
df = pd.DataFrame(data) 
corr = stats.pearsonr (experience, salary)[0] 
print("The r value is:",corr) 
if(corr>=0.7): 
 print("Positively strong relation") 
elif(corr<=-0.7): 
 print("Negatively strong relation") 
else: 
 print("No relation") 
a=np.corrcoef(experience, salary) 
plt.subplot(1,2,1) 
plt.scatter(experience,salary, c ="blue") 
plt.xlabel("experience") 
plt.ylabel("salay") 
print("The correlation Matrix is:\n",a) 
r=df['expr'].corr(df['age']) 
print("The r value is:",r) 
if(r>=0.7): 
 print("Positively strong relation") 
elif(r<=-0.7): 
 print("Negatively strong relation") 
else: 
 print("No relation") 
plt.subplot(1,2,2) 
plt.scatter(df.expr,df.age, c ="red") 
plt.xlabel("experience") 
plt.ylabel("age") 
plt.show() 