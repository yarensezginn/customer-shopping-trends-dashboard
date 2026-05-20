import pandas as pd

df = pd.read_csv("shopping_trends_cleaned.csv")

print("Customer Count by Loyalty Group")
print("----------------------")
count_by_loyalty = df["Loyalty_Group"].value_counts()
print(count_by_loyalty)

print("\nSales by Loyalty Group")
print("----------------------")
sales_by_loyalty = df.groupby("Loyalty_Group")["Purchase_Amount_USD"].sum().sort_values(ascending=False)
print(sales_by_loyalty)

print("\nAverage Purchase Amount by Loyalty Group")
print("----------------------")
avg_by_loyalty = df.groupby("Loyalty_Group")["Purchase_Amount_USD"].mean().sort_values(ascending=False)
print(avg_by_loyalty)

print("\nAverage Review Rating by Loyalty Group")
print("----------------------")
rating_by_loyalty = df.groupby("Loyalty_Group")["Review_Rating"].mean().sort_values(ascending=False)
print(rating_by_loyalty)