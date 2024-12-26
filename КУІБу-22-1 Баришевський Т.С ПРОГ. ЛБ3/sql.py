import sqlite3
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
''')
cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ("admin", "admin1"))
cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ("user", "user1"))
conn.commit()
conn.close()
