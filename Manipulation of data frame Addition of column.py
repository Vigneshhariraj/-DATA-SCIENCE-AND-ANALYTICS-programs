import pandas as pd 
data = {'ONE' : pd.Series([10, 20, 30, 40], index=[1, 2, 3, 4]), 
'TWO' : pd.Series([50, 60, 70, 80], index=[1, 2, 3, 4])} 
df = pd.DataFrame(data) 
print("------------------------") 
print("Data Frame before adding a new column") 
print(df) 
print("------------------------") 
df['THREE'] = pd.Series([90, 100, 110, 120], index=[1, 2, 3, 4]) 
print("Data Frame after adding a new column\n", df) 
print("------------------------")