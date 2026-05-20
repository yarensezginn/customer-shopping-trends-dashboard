import pandas as pd

df = pd.read_csv("shopping_trends.csv")

columns_to_check = [
    "Gender",
    "Category",
    "Location",
    "Season",
    "Subscription Status",
    "Payment Method",
    "Shipping Type",
    "Discount Applied",
    "Promo Code Used",
    "Frequency of Purchases"
]

for col in columns_to_check:
    print(f"\n--- {col} ---")
    print(df[col].value_counts())