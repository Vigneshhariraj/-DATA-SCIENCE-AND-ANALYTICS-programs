import pandas as pd

# Creating DataFrames
df1 = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])

# Display DataFrames
print("---------------------")
print("df1 :")
print(df1)
print("---------------------")
print("df2 :")
print(df2)
print("---------------------")

# Use pd.concat to combine DataFrames
print("df1 + df2 :")
df3 = pd.concat([df1, df2], ignore_index=True)
print(df3)
