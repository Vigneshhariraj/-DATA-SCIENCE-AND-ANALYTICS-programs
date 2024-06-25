import pandas as pd 
data = {'ONE' : pd.Series([10, 20, 30, 40], index=[1, 2, 3, 4]), 
'TWO' : pd.Series([50, 60, 70, 80], index=[1, 2, 3, 4])} 
df = pd.DataFrame(data)  
print("------------------------")  
print(df) 
print("------------------------") 
print("Selecting row ONE") 
print(df['ONE']) 
print("------------------------") 
print("Selecting row TWO") 
print(df['TWO']) 
print("------------------------") 