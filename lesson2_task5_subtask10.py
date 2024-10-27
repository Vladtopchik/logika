import sqlite3

connection = sqlite3.connect('secret.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE products (
                    product_id INTEGER PRIMARY KEY,
                    name TEXT,
                    price REAL
                )''')
cursor.execute('''CREATE TABLE orders (
                    order_id INTEGER PRIMARY KEY,
                    product_id INTEGER,
                    quantity INTEGER,
                    customer_id INTEGER
                )''')

cursor.executemany('INSERT INTO products (name, price) VALUES (?, ?)', [
    ('Laptop', 1200.00), ('Smartphone', 700.00), ('Headphones', 150.00), ('Tablet', 500.00)
])

cursor.executemany('INSERT INTO orders (product_id, quantity, customer_id) VALUES (?, ?, ?)', [
    (1, 5, 1), (2, 3, 2), (1, 2, 3), (3, 10, 1), (2, 8, 4), (4, 5, 3), (1, 3, 2), (3, 12, 1)
])

cursor.execute('''SELECT products.name, SUM(orders.quantity) AS total_quantity, 
                  SUM(orders.quantity * products.price) AS total_revenue
           FROM orders
           JOIN products ON orders.product_id = products.product_id
           GROUP BY products.name
           HAVING total_quantity > 10
           ORDER BY total_quantity DESC''')
results = cursor.fetchall()
for result in results:
    print(result)

connection.close()
