# Importing library 
from scipy.stats import f_oneway 
# Performance when each of the engine 
# oil is applied 
performance1 = [89, 89, 88, 78, 79] 
performance2 = [93, 92, 94, 89, 88] 
performance3 = [89, 88, 89, 93, 90] 
performance4 = [81, 78, 81, 92, 82] 
# Conduct the one-way ANOVA 
f,p_value=f_oneway(performance1, performance2, performance3, performance4) 
print(f,p_value)