import random 
import numpy as np 
import pandas as pd 
import patsy 
import matplotlib.pyplot as plt 
import statsmodels.formula.api as smf 
import statsmodels.api as sm 
from statsmodels.stats.anova import AnovaRM 
from statsmodels.regression.mixed_linear_model import MixedLMResults 
from scipy import stats 
import seaborn as sns 

subs_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10'] 
task_list = ['task1', 'task2', 'task3'] 
condition_list = ['pre', 'post'] 

# Read data into dataframe 
df_2way_rm = pd.DataFrame(columns=["sub_id", "task", "condition", "my_value"]) 
my_row = 0 
sub_id = 0 

for sub in subs_list: 
    sub_id += 1 
    for ind_t, task in enumerate(task_list): 
        for ind_c, con in enumerate(condition_list): 
            # Generate random value here as example
            my_val = np.random.normal(ind_t + ind_c, 1, 1)[0] 
            df_2way_rm.loc[my_row] = [sub_id, task, con, my_val] 
            my_row += 1 

# Print the dataframe
print(df_2way_rm) 

# Conduct ANOVA using AnovaRM
my_model_fit = AnovaRM(df_2way_rm, 'my_value', 'sub_id', within=['task', 'condition']).fit()
print(my_model_fit.anova_table)
