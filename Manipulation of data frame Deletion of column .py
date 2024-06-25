import pandas as pd

data = {'ONE': pd.Series([0, 1, 2, 3], index=[1, 2, 3, 4]),
        'TWO': pd.Series([4, 5, 6, 7], index=[1, 2, 3, 4])}

print("-----------------------")
df = pd.DataFrame(data)
print("Original DataFrame :\n", df)
print("-----------------------")

# Correct way to drop a column using `drop` with `inplace=True`
df.drop('ONE', axis=1, inplace=True)
# Alternative ways to drop a column:
# del df['ONE']         # Uncomment to use `del`
# df.pop('ONE')         # Uncomment to use `pop`

print("DataFrame after deleting a column :\n", df)
print("-----------------------")
