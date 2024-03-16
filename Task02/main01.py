import csv

def analyze_customer_data(filename):
  """
  Analyzes customer data from a CSV file and returns various insights.

  Args:
      filename: Path to the CSV file containing customer data.

  Returns:
      A dictionary containing customer insights.
  """
  data = {}
  data["num_customers"] = 0
  data["avg_customer_age"] = 0.0
  data["top_purchased_items"] = {}
  data["total_revenue"] = 0.0
  data["avg_purchase_amount"] = 0.0
  data["customers_above_amount"] = []
  data["customers_with_item"] = []
  data["spending_by_location"] = {}

  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
      # Update number of customers
      data["num_customers"] += 1

      # Calculate total customer age and average
      data["avg_customer_age"] += int(row["age"])

      # Process purchase history
      for item_name, price in zip(row["Item Name"].split(','), row["Price Per Item ($)"].split(',')):
        # Update top purchased items
        item_name = item_name.strip()  # Remove leading/trailing spaces
        if item_name not in data["top_purchased_items"]:
          data["top_purchased_items"][item_name] = 0
        data["top_purchased_items"][item_name] += 1

        # Update total revenue
        data["total_revenue"] += float(price)

      # Calculate average purchase amount per customer
      data["avg_purchase_amount"] = data["total_revenue"] / data["num_customers"] if data["num_customers"] > 0 else 0.0

  # Identify customers who spent above a certain amount
  # (Replace 100.0 with your desired amount)
  for row in reader:
    total_purchase = sum(float(price) for price in row["Price Per Items($)"].split(','))
    if total_purchase > 100.0:
      data["customers_above_amount"].append(row["customer_ID"])

  # Find customers who purchased a specific item
  # (Replace "Product X" with your desired item)
  for row in reader:
    items = row["Item Name"].split(',')
    if "Product X" in items:
      data["customers_with_item"].append(row["customer_ID"])

  # Group customers by location and calculate total spending
  for row in reader:
    location = row["location"]
    purchase_amount = sum(float(price) for price in row["Price Per Items($)"].split(','))
    if location not in data["spending_by_location"]:
      data["spending_by_location"][location] = 0.0
    data["spending_by_location"][location] += purchase_amount

  # Calculate average customer age
  data["avg_customer_age"] /= data["num_customers"] if data["num_customers"] > 0 else 1

  # Sort top purchased items by quantity (descending order)
  data["top_purchased_items"] = dict(sorted(data["top_purchased_items"].items(), key=lambda item: item[1], reverse=True)[:3])

  return data

# Replace 'data.csv' with your actual CSV file path
results = analyze_customer_data('data.csv')

# Print results
print("Number of Customers:", results["num_customers"])
print("Average Customer Age:", results["avg_customer_age"])
print("Top 3 Most Purchased Items:", results["top_purchased_items"])
print("Total Revenue Generated:", results["total_revenue"])
print("Average Purchase Amount Per Customer:", results["avg_purchase_amount"])
print("Customers who Spent Above $100:", results["customers_above_amount"])
print("Customers who Purchased 'Product X':", results["customers_with_item"])
print("Spending by Location:", results["spending_by_location"])

# Bonus: Visualization using external tools (e.g., matplotlib)
# Import libraries like matplotlib and create a bar chart here
# This requires additional code and is not included in the program

