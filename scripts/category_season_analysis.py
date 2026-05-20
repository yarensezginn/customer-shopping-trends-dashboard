import pandas as pd

df = pd.read_csv("shopping_trends_cleaned.csv")

print("Sales by Category")
print("----------------------")
sales_by_category = df.groupby("Category")["Purchase_Amount_USD"].sum().sort_values(ascending=False)
print(sales_by_category)

print("\nAverage Purchase Amount by Category")
print("----------------------")
avg_by_category = df.groupby("Category")["Purchase_Amount_USD"].mean().sort_values(ascending=False)
print(avg_by_category)

print("\nSales by Season")
print("----------------------")
sales_by_season = df.groupby("Season")["Purchase_Amount_USD"].sum().sort_values(ascending=False)
print(sales_by_season)

print("\nAverage Purchase Amount by Season")
print("----------------------")
avg_by_season = df.groupby("Season")["Purchase_Amount_USD"].mean().sort_values(ascending=False)
print(avg_by_season)