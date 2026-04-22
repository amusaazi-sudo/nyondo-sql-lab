import sqlite3

# Connect to your database file
conn = sqlite3.connect('nyondo_stock.db')

# Secure search using parameterized query
def search_product_safe(name):
    query = "SELECT * FROM products WHERE name LIKE ?"
    # Add wildcards around the name safely
    rows = conn.execute(query, (f"%{name}%",)).fetchall()
    print(f"Query: {query} | Param: {name}")
    print(f"Result: {rows}\n")
    return rows

# Secure login using parameterized query
def login_safe(username, password):
    query = "SELECT * FROM users WHERE username=? AND password=?"
    row = conn.execute(query, (username, password)).fetchone()
    print(f"Query: {query} | Params: ({username}, {password})")
    print(f"Result: {row}\n")
    return row

# Tests: all of these should return [] or None
print('Test 1:', search_product_safe("' OR 1=1--"))
print('Test 2:', search_product_safe("' UNION SELECT id,username,password,role FROM users--"))
print('Test 3:', login_safe("admin'--", 'anything'))
print('Test 4:', login_safe("' OR '1'='1", "' OR '1'='1"))
