# SQL & Python with Northwind Database

import sqlite3

# Connect to the northwind.db database
conn = sqlite3.connect('../data/northwind.db')
db = conn.cursor()

# List of Suppliers
def list_of_suppliers(db):
    query = "SELECT SupplierName FROM Suppliers;"
    db.execute(query)
    results = db.fetchall()
    return [supplier[0] for supplier in results]

# Small Orders
def count_small_orders(db):
    query = """
    SELECT COUNT(q)
    FROM (
        SELECT SUM(Quantity) as q
        FROM OrderDetails
        GROUP BY OrderId
    )
    WHERE q < 5
    """
    db.execute(query)
    result = db.fetchone()
    return result[0] if result else 0

# First Ten Products
def first_ten_products(db):
    query = """
    SELECT ProductName
    FROM Products
    ORDER BY ProductName
    LIMIT 10;
    """
    db.execute(query)
    results = db.fetchall()
    return [product[0] for product in results]

# Products with a Keyword
def products_with_keyword(db, keyword):
    query = f"""
    SELECT ProductName, SupplierName
    FROM Products
    JOIN Suppliers ON Products.SupplierID = Suppliers.SupplierID
    WHERE ProductName LIKE '%{keyword}%';
    """
    db.execute(query)
    results = db.fetchall()
    return results

# Top 5 Categories by Product Count
def top_five_categories_by_product_count(db):
    query = """
    SELECT CategoryName, COUNT(ProductID) AS ProductCount
    FROM Products
    JOIN Categories ON Products.CategoryID = Categories.CategoryID
    GROUP BY Products.CategoryID
    ORDER BY ProductCount DESC
    LIMIT 5;
    """
    db.execute(query)
    results = db.fetchall()
    return results

# Example function calls
print("\nList of Suppliers:")
print(list_of_suppliers(db))

print("\nSmall Orders:")
print(count_small_orders(db))

print("\nFirst Ten Products:")
print(first_ten_products(db))

print("\nProducts with a Keyword 'Chais':")
print(products_with_keyword(db, 'Chais'))

print("\nTop 5 Categories by Product Count:")
print(top_five_categories_by_product_count(db))

# Don't forget to close the database connection at the end of your script
conn.close()
