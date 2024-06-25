import pandas as pd
df =pd.DataFrame([[1, 2],[3, 4]], columns =['a', 'b'])
print("DataFrame :")
print(df)
df1 =df.drop(0)
print(df1)
print("DataFrame after deleting the row 0 :")
print(df)