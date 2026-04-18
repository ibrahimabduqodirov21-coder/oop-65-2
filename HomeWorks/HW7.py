import sqlite3
# CRUD = Create, Read, Update, Delete.

connect = sqlite3.connect("store.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
     name TEXT NOT NULL,
     price INTEGER NOT NULL,
     quantity INTEGER NOT NULL)
''')
connect.commit()

# 1 - Create
def create_product(name, price, quantity):
    connect.execute(
        'INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)',
        (name, price, quantity)
    )

    connect.commit()
    print('User created !')
# create_product('banana', 22, 5)

# 2 - Read
def read_products():
    cursor.execute('SELECT * FROM products')
    c = cursor.fetchall()
    print(f'All products\n {c}')
read_products()

# 3 - Update
def update_product(new_price, id):
    cursor.execute(
        'UPDATE products SET price=? WHERE id=?',
        (new_price, id)
    )
    connect.commit()
    print('User updated !')
# update_product(20, 2)

# 4 - Delete
def delete_product(id):
    cursor.execute('DELETE FROM products WHERE id=?',
                   (id,)
    )
    connect.commit()
    print('User deleted !')
delete_product(2)
