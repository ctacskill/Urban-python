import sqlite3
from distutils.command.check import check

connection = sqlite3.connect('Products.db')
connection = sqlite3.connect('Users.db')
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

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        ''')


def get_all_products():
    products = cursor.execute('SELECT * FROM Products').fetchall()
    print(products)
    return products

def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', 1000))
    connection.commit()

def is_included(username):
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if check_user.fetchone() is None:
        return False
    else:
        return True

initiate_bd()
connection.commit()
