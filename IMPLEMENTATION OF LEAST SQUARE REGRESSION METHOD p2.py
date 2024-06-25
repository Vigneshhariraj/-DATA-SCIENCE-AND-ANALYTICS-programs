import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression 
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1)) 
y = np.array([5, 20, 14, 32, 22, 38]) 
model = LinearRegression().fit(x, y) 
r_sq = model.score(x, y) 
print(f"coefficient of determination: {r_sq}") 
y_pred = model.predict(x) 
print(f"predicted response:\n{y_pred}") 
plt.scatter(x,y, color = "m",marker = "o", s = 30) 
plt.plot(x, y_pred, color = "green") 
plt.xlabel('x') 
plt.ylabel('y') 
plt.show() 