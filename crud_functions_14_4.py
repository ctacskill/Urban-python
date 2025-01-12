import sqlite3


connection = sqlite3.connect('Products.db')
cursor = connection.cursor()


def initiate_bd():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')


def get_all_products():
    products = cursor.execute('SELECT * FROM Products').fetchall()
    print(products)
    return products


connection.commit()
