
#I take thi sdata from chatgpt because it take a lot fo time to write it manually

from db_connection import get_connection


conn, cur = get_connection()

# Insert 3 customers
cur.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", ("Ali", "ali@example.com"))
cur.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", ("Sara", "sara@example.com"))
cur.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", ("Ahmed", "ahmed@example.com"))

# Insert orders for each 
cur.execute("INSERT INTO orders (customer_id, product_name, amount) VALUES (%s, %s, %s)", (1, "Laptop", 2500.00))
cur.execute("INSERT INTO orders (customer_id, product_name, amount) VALUES (%s, %s, %s)", (1, "Mouse", 50.00))
cur.execute("INSERT INTO orders (customer_id, product_name, amount) VALUES (%s, %s, %s)", (2, "Keyboard", 200.50))
cur.execute("INSERT INTO orders (customer_id, product_name, amount) VALUES (%s, %s, %s)", (2, "Monitor", 2100.00))
cur.execute("INSERT INTO orders (customer_id, product_name, amount) VALUES (%s, %s, %s)", (3, "Chair", 300.00))

conn.commit()
conn.close()