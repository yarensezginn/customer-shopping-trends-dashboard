import pandas as pd

df = pd.read_csv("shopping_trends_cleaned.csv")

print("Customer Count by Age Group")
print("----------------------")
count_by_age = df["Age_Group"].value_counts().sort_index()
print(count_by_age)

print("\nSales by Age Group")
print("----------------------")
sales_by_age = df.groupby("Age_Group")["Purchase_Amount_USD"].sum().sort_values(ascending=False)
print(sales_by_age)

print("\nAverage Purchase Amount by Age Group")
print("----------------------")
avg_by_age = df.groupby("Age_Group")["Purchase_Amount_USD"].mean().sort_values(ascending=False)
print(avg_by_age)

print("\nAverage Previous Purchases by Age Group")
print("----------------------")
previous_by_age = df.groupby("Age_Group")["Previous_Purchases"].mean().sort_values(ascending=False)
print(previous_by_age)

print("\nAverage Review Rating by Age Group")
print("----------------------")
rating_by_age = df.groupby("Age_Group")["Review_Rating"].mean().sort_values(ascending=False)
print(rating_by_age)