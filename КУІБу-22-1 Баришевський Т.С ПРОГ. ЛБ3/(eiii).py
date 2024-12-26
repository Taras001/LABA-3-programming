import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)
def get_db_connection():
    conn = sqlite3.connect('catalog.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM catalog').fetchall()
    conn.close()
    return jsonify([dict(item) for item in items])
if __name__ == '__main__':
    app.run(debug=True)