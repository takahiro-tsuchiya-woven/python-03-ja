### 1. Employee Age Analysis:

import pandas as pd
import sqlite3
from datetime import datetime

# Connecting to the SQLite database
conn = sqlite3.connect('../data/northwind.db')

# Reading data from the Employees table
df_employees = pd.read_sql_query("SELECT * FROM Employees", conn)

# Calculating age
current_year = datetime.now().year
df_employees['BirthDate'] = pd.to_datetime(df_employees['BirthDate'])
df_employees['Age'] = current_year - df_employees['BirthDate'].dt.year

# Calculating average age, median, mode, and standard deviation of age
average_age = df_employees['Age'].mean()
median_age = df_employees['Age'].median()
mode_age = df_employees['Age'].mode()[0]
std_dev_age = df_employees['Age'].std()

print(f"Average Age: {average_age}, Median Age: {median_age}, Mode Age: {mode_age}, Std Dev Age: {std_dev_age}")


### 2. Customer Geography Analysis:

# Reading data from the Customers table
df_customers = pd.read_sql_query("SELECT * FROM Customers", conn)

# Grouping by Country
country_group = df_customers.groupby('Country').size()

# Computing count of customers per country and identifying extremes
print(country_group)
print(f"Country with most customers: {country_group.idxmax()}, Count: {country_group.max()}")
print(f"Country with least customers: {country_group.idxmin()}, Count: {country_group.min()}")


### 3. Order Timeframe Insights:

# Reading data from the Orders table
df_orders = pd.read_sql_query("SELECT * FROM Orders", conn)

# Converting OrderDate to datetime
df_orders['OrderDate'] = pd.to_datetime(df_orders['OrderDate'])

# Calculating average time between orders
order_date_diff = df_orders['OrderDate'].diff().dt.days.dropna()
average_order_time = order_date_diff.mean()

# Using describe() on OrderDate
order_date_description = df_orders['OrderDate'].describe()

print(f"Average time between orders: {average_order_time} days")
print(order_date_description)

### 4. Supplier Product Price Comparison:

# Reading data from the Products and Suppliers tables
df_products = pd.read_sql_query("SELECT * FROM Products", conn)
df_suppliers = pd.read_sql_query("SELECT * FROM Suppliers", conn)

# Joining tables on SupplierID
df_merged = pd.merge(df_products, df_suppliers, on='SupplierID')

# Comparing average product price per supplier
average_price_per_supplier = df_merged.groupby('SupplierName')['Price'].mean()

print(average_price_per_supplier)


# These solutions provide hands-on examples of how to use Python and Pandas to analyze data from the Northwind database, helping to develop skills in data manipulation and analysis.

# ### 5**. Comparative Analysis:**

# **Objective:** Compare two related columns and discuss patterns or relationships.

# - **Data Source:** **`Orders`** and **`OrderDetails`** tables, focusing on **`OrderDate`** and **`Quantity`**.
# - **Task:** Compare **`OrderDate`** from **`Orders`** with **`Quantity`** from **`OrderDetails`**.


# Load data from Orders and OrderDetails tables
orders = pd.read_sql_query("SELECT OrderID, OrderDate FROM Orders", conn)
order_details = pd.read_sql_query("SELECT OrderID, Quantity FROM OrderDetails", conn)

# Merge tables on OrderID
merged_data = pd.merge(orders, order_details, on='OrderID')

# Analysis: For instance, find average Quantity per month/year
merged_data['OrderDate'] = pd.to_datetime(merged_data['OrderDate'])
merged_data['YearMonth'] = merged_data['OrderDate'].dt.to_period('M')
avg_quantity_per_month = merged_data.groupby('YearMonth')['Quantity'].mean()

# Print results
print(avg_quantity_per_month)
