import pandas as pd 
data = [['name1', 21, 'name1@gmail.com', 1234567891], ['name2', 26, 'name2@gmail.com', 1234567892]] 
df = pd.DataFrame(data, columns=['NAME', 'AGE', 'EMAIL ID', 'pHONE NUMBER'], index=[1, 2]) 
print(df) 