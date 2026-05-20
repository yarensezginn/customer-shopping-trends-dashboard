import pandas as pd

df = pd.read_csv("shopping_trends_cleaned.csv")

print("Sales by Subscription Status")
print("----------------------")
sales_by_subscription = df.groupby("Subscription_Status")["Purchase_Amount_USD"].sum().sort_values(ascending=False)
print(sales_by_subscription)

print("\nAverage Purchase Amount by Subscription Status")
print("----------------------")
avg_by_subscription = df.groupby("Subscription_Status")["Purchase_Amount_USD"].mean().sort_values(ascending=False)
print(avg_by_subscription)

print("\nAverage Previous Purchases by Subscription Status")
print("----------------------")
previous_by_subscription = df.groupby("Subscription_Status")["Previous_Purchases"].mean().sort_values(ascending=False)
print(previous_by_subscription)

print("\nAverage Review Rating by Subscription Status")
print("----------------------")
rating_by_subscription = df.groupby("Subscription_Status")["Review_Rating"].mean().sort_values(ascending=False)
print(rating_by_subscription)

print("\nCustomer Count by Subscription Status")
print("----------------------")
count_by_subscription = df["Subscription_Status"].value_counts()
print(count_by_subscription)