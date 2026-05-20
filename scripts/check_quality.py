import pandas as pd

df = pd.read_csv("shopping_trends.csv")

print("Missing values:")
print(df.isnull().sum())

print("\nNumeric summary:")
print(df[[
    "Age",
    "Purchase Amount (USD)",
    "Review Rating",
    "Previous Purchases"
]].describe())