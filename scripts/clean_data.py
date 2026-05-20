import pandas as pd

# Load original dataset
df = pd.read_csv("shopping_trends.csv")

# Rename columns for easier Power BI use
df = df.rename(columns={
    "Customer ID": "Customer_ID",
    "Item Purchased": "Item_Purchased",
    "Purchase Amount (USD)": "Purchase_Amount_USD",
    "Review Rating": "Review_Rating",
    "Subscription Status": "Subscription_Status",
    "Payment Method": "Payment_Method",
    "Shipping Type": "Shipping_Type",
    "Discount Applied": "Discount_Applied",
    "Promo Code Used": "Promo_Code_Used",
    "Previous Purchases": "Previous_Purchases",
    "Preferred Payment Method": "Preferred_Payment_Method",
    "Frequency of Purchases": "Frequency_of_Purchases"
})

# Create age groups
def create_age_group(age):
    if age <= 24:
        return "18-24"
    elif age <= 34:
        return "25-34"
    elif age <= 44:
        return "35-44"
    elif age <= 54:
        return "45-54"
    elif age <= 64:
        return "55-64"
    else:
        return "65+"

df["Age_Group"] = df["Age"].apply(create_age_group)

# Create loyalty groups based on previous purchases
def create_loyalty_group(previous_purchases):
    if previous_purchases <= 10:
        return "New / Low Loyalty"
    elif previous_purchases <= 25:
        return "Developing Customer"
    elif previous_purchases <= 40:
        return "Loyal Customer"
    else:
        return "High-Value Loyal Customer"

df["Loyalty_Group"] = df["Previous_Purchases"].apply(create_loyalty_group)

# Clean frequency labels
df["Frequency_Cleaned"] = df["Frequency_of_Purchases"].replace({
    "Fortnightly": "Bi-Weekly"
})

# Save cleaned dataset
df.to_csv("shopping_trends_cleaned.csv", index=False)

print("Cleaned dataset created successfully!")
print(df.head())