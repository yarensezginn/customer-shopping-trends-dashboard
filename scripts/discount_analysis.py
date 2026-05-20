import pandas as pd

df = pd.read_csv("shopping_trends_cleaned.csv")

print("Sales by Discount Applied")
print("----------------------")
sales_by_discount = df.groupby("Discount_Applied")["Purchase_Amount_USD"].sum().sort_values(ascending=False)
print(sales_by_discount)

print("\nAverage Purchase Amount by Discount Applied")
print("----------------------")
avg_by_discount = df.groupby("Discount_Applied")["Purchase_Amount_USD"].mean().sort_values(ascending=False)
print(avg_by_discount)

print("\nAverage Previous Purchases by Discount Applied")
print("----------------------")
previous_by_discount = df.groupby("Discount_Applied")["Previous_Purchases"].mean().sort_values(ascending=False)
print(previous_by_discount)

print("\nAverage Review Rating by Discount Applied")
print("----------------------")
rating_by_discount = df.groupby("Discount_Applied")["Review_Rating"].mean().sort_values(ascending=False)
print(rating_by_discount)

print("\nCustomer Count by Discount Applied")
print("----------------------")
count_by_discount = df["Discount_Applied"].value_counts()
print(count_by_discount)