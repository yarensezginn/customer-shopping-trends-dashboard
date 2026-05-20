import pandas as pd

df = pd.read_csv("shopping_trends_cleaned.csv")

total_sales = df["Purchase_Amount_USD"].sum()
total_customers = df["Customer_ID"].nunique()
average_purchase = df["Purchase_Amount_USD"].mean()
average_rating = df["Review_Rating"].mean()
total_previous_purchases = df["Previous_Purchases"].sum()

most_popular_category = df["Category"].value_counts().idxmax()
most_popular_season = df["Season"].value_counts().idxmax()

print("Basic KPIs")
print("----------------------")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Customers: {total_customers:,}")
print(f"Average Purchase Amount: ${average_purchase:.2f}")
print(f"Average Review Rating: {average_rating:.2f}")
print(f"Total Previous Purchases: {total_previous_purchases:,}")
print(f"Most Popular Category: {most_popular_category}")
print(f"Most Popular Season: {most_popular_season}")