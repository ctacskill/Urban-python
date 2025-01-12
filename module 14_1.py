import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

def add_user():
    for i in range(1, 11):
        cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                       (f'user{i}', f'example{i}@gmail.com', i * 10 , 1000))


def update_balance():
    users = cursor.execute('SELECT * FROM Users').fetchall()
    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, 1))
    for user in users:
        if user[0] % 2 == 0:
            pass
        else:
            cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, user[0]))
        print(user)


def delete_user():
    users = cursor.execute('SELECT * FROM Users').fetchall()
    counter = 1
    for user in users:
        cursor.execute('DELETE FROM Users WHERE id = ?', (counter,))
        counter += 3

def select_users():
    users = cursor.execute('SElECT username, email, age, balance FROM Users WHERE age != ?', (60,))
    for user in users:
        print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

# -----------------------------------------------------------------
# module_14_2

def avg_balance():
    all_ = cursor.execute('SELECT COUNT(*) FROM Users').fetchone()
    sum_ = cursor.execute('SELECT SUM(balance) FROM Users').fetchone()
    avg = sum_[0] / all_[0]
    print(avg)

avg_balance()
connection.commit()
connection.close()