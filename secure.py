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



import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

# Validation helpers
def valid_name(name):
    if not isinstance(name, str):
        print("Error: name must be a string")
        return False
    if len(name) < 2:
        print("Error: name must be at least 2 characters")
        return False
    if any(c in name for c in "<>;"):
        print("Error: name contains invalid characters")
        return False
    return True

def valid_price(price):
    try:
        val = float(price)
        if val <= 0:
            print("Error: price must be greater than 0")
            return False
        return True
    except ValueError:
        print("Error: price must be a number")
        return False

def valid_username(username):
    if not isinstance(username, str):
        print("Error: username must be a string")
        return False
    if " " in username:
        print("Error: username must not contain spaces")
        return False
    if len(username) == 0:
        print("Error: username cannot be empty")
        return False
    return True

def valid_password(password):
    if not isinstance(password, str):
        print("Error: password must be a string")
        return False
    if len(password) < 6:
        print("Error: password must be at least 6 characters")
        return False
    return True

# Secure search with validation
def search_product_safe(name):
    if not valid_name(name):
        return None
    query = "SELECT * FROM products WHERE name LIKE ?"
    rows = conn.execute(query, (f"%{name}%",)).fetchall()
    print(f"Query: {query} | Param: {name}")
    print(f"Result: {rows}\n")
    return rows

# Secure login with validation
def login_safe(username, password):
    if not valid_username(username) or not valid_password(password):
        return None
    query = "SELECT * FROM users WHERE username=? AND password=?"
    row = conn.execute(query, (username, password)).fetchone()
    print(f"Query: {query} | Params: ({username}, {password})")
    print(f"Result: {row}\n")
    return row

# Test cases
print("Test 1:", search_product_safe("cement"))        # works
print("Test 2:", search_product_safe(""))              # rejected
print("Test 3:", search_product_safe("<script>"))      # rejected
print("Test 4:", login_safe("admin", "admin123"))      # works
print("Test 5:", login_safe("admin", "ab"))            # rejected
print("Test 6:", login_safe("ad min", "pass123"))      # rejected
