import pandas as pd 
data = {'ONE' : pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd']), 
'TWO' : pd.Series([4, 5, 6, 7], index=['a', 'b', 'c', 'd'])} 
print("-----------------------")  
df = pd.DataFrame(data) 
print("DataFrame :\n", df) 
print("-----------------------") 
print("row 'c' :") 
print(df.loc['c']) 
print("-----------------------") 