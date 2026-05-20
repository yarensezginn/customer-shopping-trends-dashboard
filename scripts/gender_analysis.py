import pandas as pd

df = pd.read_csv("shopping_trends_cleaned.csv")

print("Customer Count by Gender")
print("----------------------")
count_by_gender = df["Gender"].value_counts()
print(count_by_gender)

print("\nSales by Gender")
print("----------------------")
sales_by_gender = df.groupby("Gender")["Purchase_Amount_USD"].sum().sort_values(ascending=False)
print(sales_by_gender)

print("\nAverage Purchase Amount by Gender")
print("----------------------")
avg_by_gender = df.groupby("Gender")["Purchase_Amount_USD"].mean().sort_values(ascending=False)
print(avg_by_gender)

print("\nAverage Previous Purchases by Gender")
print("----------------------")
previous_by_gender = df.groupby("Gender")["Previous_Purchases"].mean().sort_values(ascending=False)
print(previous_by_gender)

print("\nAverage Review Rating by Gender")
print("----------------------")
rating_by_gender = df.groupby("Gender")["Review_Rating"].mean().sort_values(ascending=False)
print(rating_by_gender)