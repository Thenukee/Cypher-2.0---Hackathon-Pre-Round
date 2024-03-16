import pandas as pd

# Read the CSV file
df = pd.read_csv("data.csv")

# Number of Customers
num_customers = df.shape[0]

# Average Customer Age
average_age = df["age"].mean()

# Number of Customers in a Specific Age Range (e.g., 25-35 years old)
age_range_customers = df[(df["age"] >= 25) & (df["age"] <= 35)].shape[0]

# Top 3 Most Purchased Items
item_counts = df["purchase_history"].str.split(";").explode().str.split(",", expand=True)[0].value_counts()
top_items = item_counts.nlargest(3)

# Total Revenue Generated
total_revenue = df["purchase_history"].str.split(";").explode().str.split(",", expand=True)[1].astype(float).sum()

# Average Purchase Amount Per Customer
average_purchase_per_customer = total_revenue / num_customers

# Identify Customers who Spent Above a Certain Amount (e.g., $100)
high_spenders = df.loc[df["purchase_history"].str.split(";").explode().str.split(",", expand=True)[1].astype(float) > 100, "customer_id"].tolist()

# Find Customers who Purchased a Specific Item (e.g., "Laptop")
specific_item = "Laptop"
customers_with_specific_item = df[df["purchase_history"].str.contains(specific_item, na=False)]["customer_id"].tolist()

# Group Customers by Location & Calculate Total Spending per Location
total_spending_per_location = df.groupby("location")["purchase_history"].apply(
    lambda x: x.str.split(";").explode().str.split(",", expand=True)[1].astype(float).sum()
)

# Print the results
print(f"Number of Customers: {num_customers}")
print(f"Average Customer Age: {average_age:.2f}")
print(f"Number of Customers in a Specific Age Range (25-35 years old): {age_range_customers}")
print(f"Top 3 Most Purchased Items:\n{top_items}")
print(f"Total Revenue Generated: ${total_revenue:.2f}")
print(f"Average Purchase Amount Per Customer: ${average_purchase_per_customer:.2f}")
print(f"Customers who Spent Above $100: {high_spenders}")
print(f"Customers who Purchased {specific_item}:\n{customers_with_specific_item}")
print(f"Total Spending per Location:\n{total_spending_per_location}")
 