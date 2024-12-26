from flask import Flask, jsonify, request, Response
from functools import wraps

app = Flask(__name__)
def load_users():
    users = {}
    with open("users.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(":")
            users[username] = password
    return users
users = load_users()
catalog = [
    {"id": 1, "name": "Coffe", "price": "50"},
    {"id": 2, "name": "Coffe2", "price": "55"},
    {"id": 3, "name": "Coffe3", "price": "60"}
]
def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username in users and users[auth.username] == auth.password:
            return func(*args, **kwargs)
        return Response("Потрібна автентифікація!", status=401, headers={"WWW-Authenticate": "Basic"})
    return wrapper

@app.route('/items', methods=['GET'])
@authenticate
def get_items():
    return jsonify(catalog)
@app.route('/items/<int:item_id>', methods=['GET'])
@authenticate
def get_item(item_id):
    item = next((i for i in catalog if i["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

if __name__ == '__main__':
    app.run(debug=True)