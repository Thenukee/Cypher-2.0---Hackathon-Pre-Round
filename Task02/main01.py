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
  data["age_range_count"] = 0
  data["top_purchased_items"] = {}
  data["total_revenue"] = 0.0
  data["avg_purchase_amount"] = 0.0
  data["customers_above_amount"] = []
  data["customers_with_item"] = []
  data["spending_by_location"] = {}

  with open(filename, 'r') as file:
    reader = csv.reader(file)
    # Skip the header row (assuming headers are present)
    next(reader)

    for row in reader:
      # Extract data from each row
      customer_id, name, age, location, purchase_history, item_prices = row

      # Calculate number of customers
      data["num_customers"] += 1

      # Calculate average customer age (handle potential non-numeric values)
      try:
        data["avg_customer_age"] += int(age)
      except ValueError:
        pass  # Skip rows with invalid age data

      # Calculate number of customers in a specific age range
      if 25 <= int(age) <= 35:
        data["age_range_count"] += 1

      # Calculate top 3 most purchased items
      for purchase in purchase_history.split(', '):
        item, quantity = purchase.split(':')
        if item in data["top_purchased_items"]:
          data["top_purchased_items"][item] += int(quantity)
        else:
          data["top_purchased_items"][item] = int(quantity)

      # Calculate total revenue generated
      for item in item_prices.split(', '):
        item_name, price = item.split(':')
        data["total_revenue"] += int(quantity) * float(price)

      # Calculate average purchase amount per customer
      total_purchase = sum([int(quantity) * float(price) for item, quantity, price in zip(purchase_history.split(', '), item_prices.split(', '))])
      data["total_purchase_amount"] += total_purchase

      # Identify customers who spent above a certain amount
      if total_purchase > 100.0:
        data["customers_above_amount"].append(customer_id)

      # Find customers who purchased a specific item
      if 'Product X' in item_prices:
        data["customers_with_item"].append(customer_id)

      # Group customers by location & calculate total spending per location
      location = row[3]
      if location in data["spending_by_location"]:
        data["spending_by_location"][location] += total_purchase
      else:
        data["spending_by_location"][location] = total_purchase

  # Calculate average customer age (avoid division by zero)
  data["avg_customer_age"] /= data["num_customers"] if data["num_customers"] > 0 else 1

  # Sort top purchased items by quantity (descending order)
  data["top_purchased_items"] = dict(sorted(data["top_purchased_items"].items(), key=lambda item: item[1], reverse=True)[:3])

  return data

# Replace 'data.csv' with your actual CSV file path
results = analyze_customer_data('data.csv')

# Print the results
print("Number of Customers:", results["num_customers"])
print("Average Customer Age:", results["avg_customer_age"])
print("Number of Customers in a Specific Age Range:", results["age_range_count"])
print("Top 3 Most Purchased Items:", results["top_purchased_items"])
print("Total Revenue Generated: $", results["total_revenue"])
print("Average Purchase Amount Per Customer: $", results["total_purchase_amount"] / results["num_customers"])

