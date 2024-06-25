from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# Creating the distribution
data = np.arange(1, 10, 0.01)
pdf = norm.pdf(data, loc=5.3, scale=1)

# Setting the style
sb.set_style('whitegrid')

# Visualizing the distribution using seaborn
sb.lineplot(x=data, y=pdf, color='black')

# Adding labels
plt.xlabel('Heights')
plt.ylabel('Probability Density')

# Showing the plot
plt.show()
