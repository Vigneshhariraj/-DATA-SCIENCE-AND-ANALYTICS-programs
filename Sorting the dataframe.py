import pandas as pd 
data = {'Name' : ['name1', 'name2', 'name3'], 'Age' : [20, 21, 22]} 
df = pd.DataFrame(data)  
print("\nDataset before sorting :\n", df) 
d_sort1 = df.sort_values(by='Name') 
print("\nDataset after sorted by Name :\n", d_sort1) 
d_sort2 = df.sort_values(by='Age') 
print("\nDataset after sorted by Age :\n", d_sort2)