import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tabulate import tabulate

# Read the CSV file
data = pd.read_csv('csvq.csv')

# Number of Customers
num_customers = data['customer_id'].nunique()

# Average Customer Age
avg_age = data['age'].mean()

# Number of Customers in a Specific Age Range
age_range_count = data[(data['age'] >= 25) & (data['age'] <= 35)]['customer_id'].count()

# Top 3 Most Purchased Items
items = data['purchase_history'].str.split(';', expand=True)
items = items.stack().str.split(',', expand=True)
items.columns = ['Item Name', 'Quantity']
items['Quantity'] = pd.to_numeric(items['Quantity'])
top_items = items.groupby('Item Name')['Quantity'].sum().nlargest(3)

# Total Revenue Generated
# Split purchase history into items and quantities
items = data['purchase_history'].str.split(';', expand=True)
items = items.stack().str.split(',', expand=True)
items.columns = ['Item Name', 'Quantity']
items['Quantity'] = pd.to_numeric(items['Quantity'])

# Reset index of 'items' dataframe
items.reset_index(inplace=True, drop=True)

# Merge 'items' with 'data' on the index
merged_data = pd.concat([data, items], axis=1)

total_revenue = (merged_data['Quantity'] * merged_data['Price Per Item ($)']).sum()

# Average Purchase Amount Per Customer
avg_purchase_per_customer = total_revenue / num_customers

# Identify Customers who Spent Above a Certain Amount
high_spending_customers = data.groupby('customer_id')['purchase_history'].sum()
high_spending_customers = high_spending_customers[high_spending_customers.apply(lambda x: sum([int(i.split(',')[1]) for i in x.split(';')])) > 100]

# Find Customers who Purchased a Specific Item
specific_item = 'Watch'
# Replace NaN values in 'purchase_history' with empty strings
data['purchase_history'] = data['purchase_history'].fillna('')
customers_purchased_item = data[data['purchase_history'].str.contains(specific_item)]['customer_id']

# Convert customer_id to integer
customers_purchased_item = customers_purchased_item.astype(int)

# Remove newline characters from the 'purchase_history' column
high_spending_customers = high_spending_customers.str.replace('\n', '')

# Top 5 Most Purchased Items
items = data['purchase_history'].str.split(';', expand=True)
items = items.stack().str.split(',', expand=True)
items.columns = ['Item Name', 'Quantity']
items['Quantity'] = pd.to_numeric(items['Quantity'])
top_items = items.groupby('Item Name')['Quantity'].sum().nlargest(5)

# Create a bar chart
fig, ax = plt.subplots(figsize=(6, 4), dpi=80)
top_items.plot(kind='bar', color='skyblue', ax=ax)
ax.set_xlabel('Item Name')
ax.set_ylabel('Quantity')
ax.set_title('Top 5 Most Purchased Items')
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()

# GUI
root = tk.Tk()
root.title('Marketing Campaign Analysis')

# CLI output
cli_output = tk.Text(root, height=40, width=100)
cli_output.insert(tk.END, f'Number of Customers: {num_customers}\n')
cli_output.insert(tk.END, f'Average Customer Age: {avg_age}\n')
cli_output.insert(tk.END, f'Number of Customers in the Age Range 25-35: {age_range_count}\n')
cli_output.insert(tk.END, 'Top 3 Most Purchased Items:\n')
cli_output.insert(tk.END, tabulate(top_items.to_frame(), headers='keys', tablefmt='psql'))
cli_output.insert(tk.END, f'\nTotal Revenue Generated: {total_revenue}\n')
cli_output.insert(tk.END, f'Average Purchase Amount Per Customer: {avg_purchase_per_customer}\n')
cli_output.insert(tk.END, 'Customers who Spent Above $100:\n')
cli_output.insert(tk.END, tabulate(high_spending_customers.to_frame(), headers='keys', tablefmt='psql'))
cli_output.insert(tk.END, f'\nCustomers who Purchased {specific_item}:\n')
cli_output.insert(tk.END, tabulate(customers_purchased_item.to_frame(), headers='keys', tablefmt='psql'))
cli_output.grid(row=0, column=0, padx=10, pady=10)

# Graph
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=1, padx=10, pady=10)

root.mainloop()
