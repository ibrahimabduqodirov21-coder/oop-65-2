import sqlite3

# A4
connect = sqlite3.connect("users.db")
# Рука с ручкой
cursor = connect.cursor()

#     11       id INTEGER PRIMARY KEY AUTOINCREMENT,
cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            name VARCHAR(50) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT  
        )
''')
connect.commit()

# CRUD Create - Read - Update - Delete

def create_user(name, age, hobby):
    # cursor.execute(f'INSERT INTO users (name, age, hobby) VALUES ("{name}", "{age}", "{hobby}")')
    connect.execute(
        'INSERT INTO users (name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )

    connect.commit()
    print("User created successfully")
create_user("Ibrahim", 18, "Relax")

def read_users():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    print(f'all users\n {data}')
read_users()

def update_user(new_name, rowid):
    cursor.execute(
        'UPDATE users SET name = ? WHERE rowid = ?',
        (new_name, rowid)
    )
    connect.commit()
    print("User updated !!")
update_user('Brahim', 2)
read_users()

def delete_user(rowid):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (rowid,)
    )
    connect.commit()
    print("User deleted !!")
delete_user(2)

