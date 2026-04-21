import sqlite3

# Connect to database (replace 'store.db' with your actual DB file)
conn = sqlite3.connect("store.db")
cursor = conn.cursor()

# Query A: Get every column of every product
cursor.execute("SELECT * FROM products;")
print("Query A:", cursor.fetchall())

# Query B: Get only the name and price of all products
cursor.execute("SELECT name, price FROM products;")
print("Query B:", cursor.fetchall())

# Query C: Get full details of the product with id = 3
cursor.execute("SELECT * FROM products WHERE id = 3;")
print("Query C:", cursor.fetchall())

# Query D: Find all products whose name contains 'sheet'
cursor.execute("SELECT * FROM products WHERE name LIKE '%sheet%';")
print("Query D:", cursor.fetchall())

# Query E: Get all products sorted by price, highest first
cursor.execute("SELECT * FROM products ORDER BY price DESC;")
print("Query E:", cursor.fetchall())

# Query F: Get only the 2 most expensive products
cursor.execute("SELECT * FROM products ORDER BY price DESC LIMIT 2;")
print("Query F:", cursor.fetchall())

# Query G: Update the price of Cement (id=1) to 38000 then confirm
cursor.execute("UPDATE products SET price = 38000 WHERE id = 1;")
conn.commit()
cursor.execute("SELECT * FROM products;")
print("Query G:", cursor.fetchall())

conn.close()
