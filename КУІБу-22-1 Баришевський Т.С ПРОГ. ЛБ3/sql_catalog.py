import sqlite3
conn = sqlite3.connect('catalog.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS catalog (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price TEXT NOT NULL
)
''')
items = [
    (1, 'Coffe', '50'),
    (2, 'Coffe2', '55'),
    (3, 'Coffe3', '60')
]
cursor.executemany('INSERT INTO catalog (id, name, price) VALUES (?, ?, ?)', items)
conn.commit()
conn.close()