import pandas as pd

df = pd.read_csv('shopping_trends.csv')

print("Column names:")
print(df.columns.tolist())

print("\nDataset shape:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())